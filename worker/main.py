"""Celeryワーカーアプリケーションの設定とタスク定義"""

import os
from celery import Celery

# Redisをブローカーとして使用するCeleryアプリケーションを作成
app = Celery(
    "celery_worker",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
)

# Celeryの設定
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    task_acks_late=True,
    broker_transport_options={"queue_order_strategy": "sorted"},
    timezone="Asia/Tokyo",
    enable_utc=True,
)


@app.task(name="celery_worker.add")
def add(x: int, y: int) -> int:
    """サンプルタスク: 2つの数値を足し算する"""
    return x + y


@app.task(name="celery_worker.multiply")
def multiply(x: int, y: int) -> int:
    """サンプルタスク: 2つの数値を掛け算する"""
    return x * y

