from django.shortcuts import render
from .models import NewsArticle
from news_aggregator import settings
import requests

from . import uuid

api_url = "https://newsapi.org/v2/top-headlines"


def basicNews(request):

    params = {
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    # try to save all the uuid from database into a dict
    # add a reference and time
    # method overloading - fix
    # try to work on github and merge the progress
    # Unit testing needs to be included - news/test/testing

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )

            #try to save all uuids to csv / text file - cache
    
    allData= NewsArticle.objects.all()

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def sportsNews(request):

    params = {
        'category' : 'sports',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "sports",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "sports")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def businessNews(request):

    params = {

        'category' : 'business',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "business",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "business")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def entertainmentNews(request):

    params = {
        'category' : 'entertainment',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "entertainment",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "entertainment" )

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def healthNews(request):

    params = {
        'category' : 'health',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "health",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "health")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def scienceNews(request):

    params = {
        'category' : 'science',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "science",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "science")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def technologyNews(request):

    params = {
        'category' : 'technology',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "technology",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "technology")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def indiaNews(request):

    params = {
        'country' : 'in',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "in",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "in")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def usNews(request):

    params = {
        'country' : 'us',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "us",               
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "us")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def bbcNews(request):
    
    api_url = "https://newsapi.org/v2/everything"

    params = {
        'q' : 'bbc',
        'language' : 'en',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "bbc news",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "bbc news")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})

def foxNews(request):

    api_url = "https://newsapi.org/v2/everything"

    params = {
        'q' : 'fox news',
        'apiKey' : settings.NEWS_API_KEY,
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    puraArticle =  data.get('articles', [])

    for article in puraArticle:

        kuchBhi = uuid.generateUUIDfromString(article['title']),

        if article['title'] != "[Removed]" and not(NewsArticle.objects.filter(uuid = kuchBhi).exists()):
            
            NewsArticle.objects.create(
                genre = "fox news",
                uuid = kuchBhi,
                title=article['title'],
                author=article['author'],
                description=article['description'],
                url=article['url'],
                publishedAt=article['publishedAt'],
                urlToImage = article['urlToImage'],
                
            )
    
    allData= NewsArticle.objects.filter(genre = "fox news")

    data={

        'allData' : allData
    }

    return render(request, 'news/news_by_genre.html', {'articles' : allData})