# 【シェルスクリプト】GCP に DeepLearning 環境を自動的に構築する。

## 実現方法

### Ubuntu 16.04
- `ブートディスク： Ubuntu 16.04 LTS` でイメージを作成（GPUの割り当ても行う）
- 「VM インスタンスの詳細」ページの「SSH 認証鍵」で、ローカル PC の `id_rsa.pub` を登録
- このとき、別のユーザが作成されるので、そのユーザで ssh 接続
    - デフォルトのユーザ名とは別ユーザになる。このユーザでは sudo 権限が付与されているので、`sudo` コマンド実行時にいちいちパスワードなどを入力しなくてよい
- `${HOME}` ディレクトリ以下で、以下のスクリプトを実行し、GPU ドライバ + CUDA + cuDNN + conda などをインストール
    ```sh
    $ sh install_GPU_ubuntu16.04.sh
    ```

### Ubuntu 18.04
- `ブートディスク： Ubuntu 18.04 LTS` でイメージを作成（GPUの割り当ても行う）
- 「VM インスタンスの詳細」ページの「SSH 認証鍵」で、ローカル PC の `id_rsa.pub` を登録
- このとき、別のユーザが作成されるので、そのユーザで ssh 接続
    - デフォルトのユーザ名とは別ユーザになる。このユーザでは sudo 権限が付与されているので、`sudo` コマンド実行時にいちいちパスワードなどを入力しなくてよい
- `${HOME}` ディレクトリ以下で、以下のスクリプトを実行し、GPU ドライバ + CUDA + conda などをインストール
    ```sh
    $ sh install_GPU_ubuntu18.04.sh
    ```

## 入出力データ

- xxx

## 参照サイト
- https://tech.zeals.co.jp/entry/2019/01/08/094054