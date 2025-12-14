.PHONY: help lint format check fix

help: ## このヘルプメッセージを表示
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

lint: ## ruffでコードをチェック
	uv run ruff check .

format: ## ruffでコードをフォーマット
	uv run ruff format .

fix: ## ruffで自動修正可能な問題を修正
	uv run ruff check --fix .