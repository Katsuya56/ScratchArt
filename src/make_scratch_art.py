import cv2
import numpy as np
from PIL import Image

# グラデーション画像を生成するための関数

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float64)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(
            start, stop, width, height, is_horizontal)

    return result

threshold = 110    # 閾値

base_image_path = "image/1bace.jpg"
black_white_imagepath = "image/2BW.jpg"
threshold_imagepath = f"image/3BW{threshold}.jpg"
gradient_image_path = "image/4gradient.jpg"
scratch_art_image_path = "image/5scratch_art.jpg"

# 加工元画像
bace_image = cv2.imread(base_image_path)

# 画像をグレースケール化
image_gray = cv2.cvtColor(bace_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(black_white_imagepath, image_gray)
# サイズ取得
height = image_gray.shape[0]
width = image_gray.shape[1]

# 閾値を基準に白黒化
ret, threshold_image = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
# ret, threshold_image = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY_INV)
# 白黒画像の保存
cv2.imwrite(threshold_imagepath, threshold_image)

# グラデーションの生成
gradient_RGB = get_gradient_3d(width, height, (0, 0, 192),
                           (255, 255, 64), (False, False, True))
# グラデーション画像の保存
cv2.imwrite(gradient_image_path, gradient_RGB)

# 白黒画像とグラデーション画像の合成
# 白黒画像の読み込み
img1_BGR = cv2.imread(threshold_imagepath)
img1_RGB = cv2.cvtColor(img1_BGR, cv2.COLOR_BGR2RGB)
# グラデーション画像の読み込み
img2_BGR = cv2.imread(gradient_image_path)

# 画像の合成
blended = cv2.addWeighted(src1=img1_RGB, alpha=0.7,
                          src2=img2_BGR, beta=0.3, gamma=0)
cv2.imwrite(scratch_art_image_path, blended)
