import requests
import os

LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
user_id = os.getenv('USER_ID')

def send_news_to_line(reply_token, message):
    print("test line_api.py")
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }
    data = {
        'to': user_id,
        'messages': [{'type': 'text', 'text': message}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print('Message sent')
    else:
        print(f'Error sending message: {response.status_code}')
