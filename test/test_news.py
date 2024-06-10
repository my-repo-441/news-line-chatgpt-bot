import requests
from dotenv import load_dotenv
import os

load_dotenv()  # .envファイルの読み込み

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def get_latest_news(query, page_size=10):
    url = f'https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
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

# 検証用コード
if __name__ == "__main__":
    query = "technology"
    news_articles = get_latest_news(query, page_size=10)
    
    for idx, article in enumerate(news_articles):
        print(f"{idx+1}. {article['title']}")
        print(f"Source: {article['source']}")
        print(f"Author: {article['author']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print(f"Image URL: {article['urlToImage']}")
        print(f"Published At: {article['publishedAt']}")
        print(f"Content: {article['content']}")
        print()
