import os
import logging
from datetime import datetime
from time import sleep
import asyncio
import redis
import uuid
from PIL import Image

from fastapi import FastAPI
from fastapi import BackgroundTasks
from pydantic import BaseModel
from typing import Any, Dict

import sys
sys.path.append(os.path.join(os.getcwd(), '../redis'))
from redis_client import redis_client
from redis_utils import set_image_pillow_redis, set_image_base64_redis

sys.path.append(os.path.join(os.getcwd(), '../utils'))
from utils import conv_base64_to_pillow, conv_pillow_to_base64

app = FastAPI()

# logger
logger = logging.getLogger(__name__)
logger.setLevel(10)
logger_fh = logging.FileHandler( __name__ + '.log')
logger.addHandler(logger_fh)


class ImageData(BaseModel):
    """
    画像データのリクエストボディ
    """
    image: Any

class SetDataRedisJob(BaseModel):
    """
    非同期処理での Job を定義したジョブクラス
    """
    job_id: str
    img_pillow: Any
    job_status: str = "RUNNING"

    def __call__(self):
        jobs[self.job_id] = self
        self.job_status = "RUNNING"
        try:
            # Redis キューの先頭に job_id を追加
            redis_client.lpush("job_id", self.job_id)
            print('[{}] time {} | Job {} を登録しました'.format(self.__class__.__name__, f"{datetime.now():%H:%M:%S}", self.job_id))
            logger.info('[{}] time {} | Job {} を登録しました'.format(self.__class__.__name__, f"{datetime.now():%H:%M:%S}", self.job_id))

            # 画像を追加
            set_image_pillow_redis(redis_client=redis_client, key_name=self.job_id, img_pillow=self.img_pillow)
            self.job_status = "SUCCEED"
        except Exception:
            print('[{}] time {} | Job {} の登録に失敗しました'.format(self.__class__.__name__, f"{datetime.now():%H:%M:%S}", self.job_id))
            logger.info('[{}] time {} | Job {} の登録に失敗しました'.format(self.__class__.__name__, f"{datetime.now():%H:%M:%S}", self.job_id))
            self.job_status = "FAILED"

        return

jobs : Dict[str, SetDataRedisJob] = {}

@app.get("/")
async def root():
    return 'Hello Proxy Server!\n'

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/metadata")
async def metadata():    
    return {
        "status": "ok",
        "jobs" : jobs,
    }

@app.get("/get_job/{job_id}")
async def get_job(
    job_id: str,  # パスパラメーター
):
    try:
        img_base64 = redis_client.get(job_id)
    except Exception:
        return {"status", "ジョブ {} は実行されていません".format(job_id)}

    return {
        "status": "ok",
        "job_id" : jobs[job_id].job_id,
        "job_status" : jobs[job_id].job_status,
        "img_base64" : img_base64,
    }

@app.post("/start_job")
async def start_job(
    img_data: ImageData,                # リクエストボディ
    background_tasks: BackgroundTasks,  # BackgroundTasks
):
    # job_id を自動生成
    job_id = str(uuid.uuid4())[:6]

    # base64 -> Pillow への変換
    img_data.image = conv_base64_to_pillow(img_data.image)

    # ジョブクラスのオブジェクト作成
    task = SetDataRedisJob(job_id=job_id, img_pillow=img_data.image)

    # BackgroundTasks にジョブを追加
    background_tasks.add_task(task)

    return {
        "status": "ok",
        "job_id" : task.job_id,
        "job_status" : task.job_status,
    }