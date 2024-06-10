import json
import logging
from flask import request
from app import app

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info("Received event: " + json.dumps(event))

        # LINEプラットフォームからのイベントを処理
        events = event.get('events', [])
        if not events:
            raise ValueError("No events found in the received event")

        # 最初のイベントを処理 (複数イベントが含まれる場合はループを実装)
        line_event = events[0]
        path = '/webhook'
        base_url = "https://example.com"  # 必要に応じて変更
        method = 'POST'
        headers = {'Content-Type': 'application/json'}  # 必要に応じて追加
        query_string = {}
        data = json.dumps(event)

        with app.test_request_context(
            path=path,
            base_url=base_url,
            method=method,
            headers=headers,
            query_string=query_string,
            data=data
        ):
            response = app.full_dispatch_request()
            return {
                "statusCode": response.status_code,
                "headers": dict(response.headers),
                "body": response.get_data(as_text=True)
            }
    except KeyError as e:
        logger.error(f"KeyError: {str(e)}")
        logger.error("Received event: " + json.dumps(event))
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing key: {str(e)}"})
        }
    except Exception as e:
        logger.error("Error processing request: " + str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
