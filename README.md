# MachineLearning_PreProcessing_Exercises
機械学習のための前処理の練習用コード

## ■ 動作環境

- Python : 3.6
- Anaconda : 5.0.1
- IO関係
    - xxx
- 画像処理系
    - OpenCV : 
    - Pillow :

## ■ 項目

1. 開発環境
    1. 【シェルスクリプト】シェルスクリプト内で conda 環境を切り替える。
1. 入出力処理
    1. [【シェルスクリプト】フォルダ内のファイル数を確認する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/io_processing/2)
    1. [【Python】フォルダ内のファイル一覧を取得する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/io_processing/1)
    1. [【Python】２つのフォルダのファイル数＆ファイル名の差分を確認する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/io_processing/3)
    1. [【シェルスクリプト】ランダムに１００個のファイルをサンプリングする。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/io_processing/4)
1. サーバー＆クラウド処理
    1. 【シェルスクリプト】ssh 切れ対策のために `nohup` コマンドで実行する。
    1. 【シェルスクリプト】サーバー間でデータを転送・コピーする。
    1. [【UNIX】サーバー上の画像ファイルをブラウザ上で確認する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/server_processing/2)
    1. [【シェルスクリプト】GCP or AWS インスタンスをシェルスクリプト上から停止する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/server_processing/1)
    1. 【GCP】GCP ディスクを `gcsfuse` コマンドでマウントする。
    1. 【AWS】EC インスタンスのディスク容量を後から増設する。
1. 画像処理
    1. [【シェルスクリプト】画像ファイルの解像度を確認する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/1)
    1. [【Python】OpenCV ↔ Pillow ↔ numpy の変換対応](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/4)
    1. [【Python】画像の滑らかさを落とさないように拡張子を変更する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/3)
    1. [【Python】画像やセマンティックセグメンテーション画像の滑らかさを落とさないようにリサイズする。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/2)
    1. [【Python】画像の対象物のアスペクト比を変えないまま adjust する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/11)
    1. [【Python】画像の対象物を膨張・収縮させる。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/14)
    1. [【Python】データオーギュメンションや品質評価のための画像の拡大縮小＆平行移動＆回転](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/13)
    1. [【Python】セマンティックセグメンテーション画像からラベル値を取得する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/5)
    1. [【Python】セマンティックセグメンテーション画像の特定のラベル値の部分を抜き取る。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/6)
    1. [【Python】画像のバイナリマスク画像を生成する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/9)
    1. [【Python】画像の背景部分をくり抜く。（グラフ カット）](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/10)
    1. remove bg を使用して、画像の背景部分をくり抜く。（グラフ カット）
    1. [【Python】画像の上下 or 左右対称性を検出する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/8)
    1. [【Python】品質評価のためのグリッド画像を生成する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/7)
    1. [【Python】元画像とセグメンテーション画像をアルファブレンディングで重ねて表示する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/12)
    1. 【Python】画像の特定の対象物が画面端で途切れているかを検出する。
    1. OpenPose による姿勢推定
        1. OpenPose のインストール
        1. 【Python】OpenPose の json ファイルを読み込む。
        1. 【Python】OpenPose の json ファイルを書き込む。
        1. [【Python】OpenPose の json ファイルの関節点を画像表示する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/openpose/1)
        1. 【Python】OpenPose の関節点情報に基づき、人物画像を全身部分でクロップする。
        1. 【Python】OpenPose の関節点情報に基づき、人物画像を上半身部分でクロップする。
        1. 【Python】OpenPose の関節点情報に基づき、人物画像が正面を向いているか後ろを向いているか判定する。
        1. 【Python】OpenPose の関節点情報に基づき、人物画像が半袖を着ているか長袖を着ているかを検出する。
        1. 【Python】OpenPose の関節点情報に基づき、人物セグメンテーション画像に、他の人体部位のラベルを追加する。
    1. waifu2x による画像の超解像度
        1. waifu2x のインストール
        1. waifu2x による画像の超解像度
    1. dlib による顔の landmark 検出
        1. [【Python】dlib で顔の landmark 検出を検出し、画像上に表示する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/image_processing/15)
1. 高速化処理
    1. 【シェルスクリプト】別プロセスで起動する。
    1. [【Python】for ループ内の処理を複数 CPU の並列処理で高速化する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/acceleration_processing/2)
    1. [【Python】複数 GPU での並列化のために、フォルダ内のファイルを分割し別フォルダに保存し、その後１つのフォルダに再統合する。](https://github.com/Yagami360/MachineLearning_PreProcessing_Exercises/tree/master/acceleration_processing/1)
    1. 【Python】for ではなく行列処理で画像処理を高速化する。
1. スクレイピング
1. 自然言語処理
1. 音声処理
1. Docker
    1. ディレクトリを Docker のコンテナから参照できるようにする。（`-v` オプションの使用）
    1. `docker run` 経由で作ったファイルの所有者を指定する。
    1. Docker コンテナで動作するスクリプトを nohup でも実行できるようにする。
    1. nvidia-docker
1. 機械学習フレームワーク
    1. PyTorch
        1. 【PyTorch】OpenCV ↔ Pillow ↔ numpy ↔ Tensor [PyTorch] の変換対応
        1. 【PyTorch】独自データセットの DataLoader 
1. その他処理
    1. 【シェルスクリプト】`curl` コマンドで WebAPI を直接たたく


## ■ 参考文献＆サイト
