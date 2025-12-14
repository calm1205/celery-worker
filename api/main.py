"""FastAPIアプリケーション"""

from fastapi import FastAPI
from celery import Celery
import os

app = FastAPI(title="Celery Worker API")

# Celeryアプリケーションの設定（タスクを送信するため）
celery_app = Celery(
    "celery_worker",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
)


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {"message": "Celery Worker API"}


@app.post("/tasks/add")
async def create_add_task(x: int, y: int):
    """足し算タスクを作成"""
    task = celery_app.send_task("celery_worker.add", args=[x, y])
    return {"task_id": task.id, "status": "created"}


@app.post("/tasks/multiply")
async def create_multiply_task(x: int, y: int):
    """掛け算タスクを作成"""
    task = celery_app.send_task("celery_worker.multiply", args=[x, y])
    return {"task_id": task.id, "status": "created"}


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """タスクの状態を取得"""
    result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None,
    }

