from newsapi import NewsApiClient
from django.db import IntegrityError
<<<<<<< HEAD
=======

>>>>>>> c37102f0f8c4ffa869d0ba5227352668825a51d7
from news.uuids.generateID import generateUUIDfromString 
from .models import NewsArticle
import logging
logger = logging.getLogger(__name__)

newsapi = NewsApiClient(api_key='044d9f64aa3144fd88b1bdc965218675')

<<<<<<< HEAD
=======

>>>>>>> c37102f0f8c4ffa869d0ba5227352668825a51d7
def fecthingfuncToo(query):
    
    all_articles = newsapi.get_everything(q=query, language='en')

    articleList =  all_articles.get('articles', [])

    uuidList = list(NewsArticle.objects.values_list("uuid", flat=True))

    for article in articleList:
<<<<<<< HEAD
        hashId = generateUUIDfromString(article['title'])
=======

        hashId = generateUUIDfromString(article['title'])

>>>>>>> c37102f0f8c4ffa869d0ba5227352668825a51d7
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
                logger.exception("exeception while save data in model")
                print(article['title'])
    return all_articles



