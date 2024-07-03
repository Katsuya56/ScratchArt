# make-scratch-art

画像を読み込んでスクラッチアートを作成するプログラム

# 環境構築方法

1. 仮想環境を立てる

   ```
   python -m venv .venv
   ```

1. vscode 上の Python の拡張機能が、実行する Python を仮想環境のものにするか聞いてくるので Yes を選択する

1. pipの更新

   ```
   python.exe -m pip install --upgrade pip
   ```

1. ライブラリをインストールする
   ```
   pip install -r requirements.txt
   ```

# 処理順序

1. ベースの画像を読み込む
1. ベースの画像をグレースケール化
1. グレースケール化した画像を閾値を定めて白(`#ffffff`)と黒(`#000000`) 画像をに変換
1. グラデーション画像を作成
1. グラデーション画像と白黒画像を合成

# 使っているライブラリ

requirements.txt

```text
numpy==2.0.0
opencv-python==4.10.0.84
pillow==10.4.0
```

# 自分の環境

- OS
  windows11
- Python
  3.11.1
