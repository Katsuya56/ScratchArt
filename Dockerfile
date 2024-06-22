# 使いたいPythonのバージョンに変更すること
FROM python:3.12

# タイムゾーンを日本に設定
ENV TZ=Asia/Tokyo
# タイムゾーン設定を反映
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# カレントディレクトリの変更
WORKDIR /home/Test

# すべてのファイルをコピー
COPY ./ ./

# ライブラリのインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

