# coding=utf-8
from sqlalchemy import Column, Integer, String, Float, DateTime, LargeBinary
from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.types import JSON
from sqlalchemy_imageattach.entity import Image, image_attachment

from mysql_utils.setting import Base

class JobTable(Base):
    """
    MySQL のデータベースに保存するテーブルデータを定義したモデルクラス
    """
    # クラス変数
    __tablename__ = "job_table"
    created_datetime = Column( TIMESTAMP, server_default=current_timestamp(), nullable=False,)
    updated_datetime = Column( TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), nullable=False)

    job_id = Column( String(255), primary_key=True)         # ジョブID（重複のない一意の値なので、プライマリーキーを設定し、ジョブIDに一致するテーブルを検索可能にする）
    elapsed_time = Column(Float)                            # 推論時間 [msec]
    image_in = Column(LargeBinary)                          # 入力画像
    image_out = Column(LargeBinary)                         # 出力画像
    #image_in = image_attachment('MySQLImage')
    #image_out = image_attachment('MySQLImage')

class MySQLImage(Base,Image):
    # クラス変数
    __tablename__ = "mysql_image_table"
