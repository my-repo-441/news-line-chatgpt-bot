import requests
import os
from bs4 import BeautifulSoup

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def get_latest_news(query, page_size=3):
    print("test news_api.py")
    url = f'https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for article in articles:
            # 記事のURLを使用して全文を取得
            full_content = fetch_full_article(article['url'])
            article['content'] = full_content
        return [
            {
                'source': article['source']['name'],
                'author': article['author'],
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'urlToImage': article['urlToImage'],
                'publishedAt': article['publishedAt'],
                'content': article['content']
            }
            for article in articles
        ]
    else:
        print(f'Error fetching news: {response.status_code}')
        return []
        
def fetch_full_article(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            full_text = ' '.join([para.get_text() for para in paragraphs])
            #print(full_text)
            return full_text
        else:
            print(f'Error fetching full article: {response.status_code}')
            return ''
    except Exception as e:
        print(f'An error occurred: {e}')
        return ''