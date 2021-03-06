import os

class ResidConfig:
    # クラス変数
    #host="0.0.0.0"
    host="redis-container"
    port="6379"
    database_id=0

class BatchServerConfig:
    # クラス変数
    n_workers=2
    polling_time=1  # ポーリング間隔時間 (sec単位)
    #polling_time=5  # ポーリング間隔時間 (sec単位)

class PredictServerConfig:
    # クラス変数
    host="predict-container"
    port="5001"