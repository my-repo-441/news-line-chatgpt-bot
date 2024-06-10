from flask import Flask, request, jsonify
import os
from utils.news_api import get_latest_news
from utils.chatgpt_api import get_summary_from_chatgpt
from utils.line_api import send_news_to_line

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("test app.py")
    events = request.json.get('events', [])
    print(events)
    for event in events:
        if event['type'] == 'message' and event['message']['type'] == 'text':
            user_input = event['message']['text']
            #news = get_latest_news('AI')
            news = get_latest_news(user_input)
            print(news)
            for article in news:
                print(article['content'])
                summary = get_summary_from_chatgpt(article['content'])
                #summary = get_summary_from_chatgpt(full_text)
                message = f"Title: {article['title']}\nSummary: {summary}\nURL: {article['url']}\nImage：{article['urlToImage']}"
                print(message)
                send_news_to_line(event['replyToken'], message)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=3000)
