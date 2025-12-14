# Celery Worker

## セットアップ

1. 環境変数ファイルを作成

```bash
cp .env.example .env
```

2. Docker Compose Watch で起動

```bash
docker compose watch
```

## redis

```bash
docker compose exec redis redis-cli SCAN 0
docker compose exec redis redis-cli GET celery-task-meta-04473adb-5469-4c5c-8cf4-516c5611b5f9 | jq .
```
