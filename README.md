# news-line-chatgpt-botの概要

このプロジェクトは、NewsAPIからニュースを取得し、ChatGPTで要約してLINEに送信するシステムです。
LINEからのリクエストをAPI Gatewayが受け取り、Lambdaに連携し、処理を行った後に、再度LINEにレスポンスします。

## 必要な環境

- Python 3.12
- requirements.txtに記載のライブラリ
- OpenAIのAPIキー
- NEWSAPIのAPIキー
- LINE Developersのアカウント

## セットアップ手順

1. リポジトリをクローンします。
2. Python3.12環境にて、必要なパッケージをインストールし、zipファイルにまとめ、Lambdaレイヤーとして登録します。
3. Lambda関数を作成し、ソースコードをアップロードします。
4. API GatewayとLambdaを連携します。
5. Lambdaの環境変数に、OpenAI、NEWS API、LINEアカウントのAPIキーなどを登録します。
6. LINEから欲しいニュース記事のキーワードをトーク画面から送信します。
7. LINEに送られてきたニュース記事を確認します。
