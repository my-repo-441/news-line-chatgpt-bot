import requests
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def get_summary_from_chatgpt(text):
    print("test chatgpt_api.py")
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-4o',  # 使用するモデルを指定
        "messages": [{"role":"user", "content":f'次の英語の文章を日本語でなるべき分かりやすく要約してください:\n\n{text}'}],
        'max_tokens': 2000,
        'temperature': 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    print(response)
    if response.status_code == 200:
        response_json = response.json()
        summary = response_json['choices'][0]['message']['content'].strip()
        return summary
    else:
        print(f'Error summarizing text: {response.status_code}')
        return ''
