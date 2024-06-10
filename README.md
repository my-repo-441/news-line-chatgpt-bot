# News Skill

このプロジェクトは、NewsAPIからニュースを取得し、ChatGPTで要約してLINEに送信するシステムです。

## 必要な環境

- Python 3.7以上
- Flask
- requests

## セットアップ

1. リポジトリをクローンします。
2. 必要なパッケージをインストールします。

```sh

source ~/venv/web-chatgpt-article-checker/bin/activate

pip install -r requirements.txt

python app.py

curl -X POST http://localhost:3000/webhook -H "Content-Type: application/json" -d '{"events":[{"type":"message","replyToken":"dummyToken","message":{"type":"text","text":"Hello"}}]}'