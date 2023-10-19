from newsapi import NewsApiClient
from django.db import IntegrityError
from news.uuids.generateID import generateUUIDfromString 
from .models import NewsArticle
import logging
logging.basicConfig(filename='newsapplogs.log',
                    level=10,
                    format="{asctime}:{levelname}:{filename}:{process}:{message}",
                    style='{'
                    )
newsapi = NewsApiClient(api_key='044d9f64aa3144fd88b1bdc965218675')

def fecthingfuncToo(query):
    
    all_articles = newsapi.get_everything(q=query, language='en')

    articleList =  all_articles.get('articles', [])

    uuidList = list(NewsArticle.objects.values_list("uuid", flat=True))

    for article in articleList:
        hashId = generateUUIDfromString(article['title'])
        if (article['title'] != "[Removed]") and (hashId not in uuidList):
            try:
                NewsArticle.objects.create(
                    genre = query,
                    uuid = hashId,
                    title=article['title'],
                    author=article['author'],
                    description=article['description'],
                    url=article['url'],
                    publishedAt=article['publishedAt'],
                    urlToImage = article['urlToImage'],
                )
            except IntegrityError:
                logging.exception("exeception while save data in model")
                print(article['title'])
    return all_articles



