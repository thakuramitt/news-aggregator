from django.shortcuts import render
from .models import NewsArticle
# from news_aggregator import settings

from . import fetching

    # try to save all the uuid from database into a dict
    # add a reference and time
    # method overloading - fix
    # try to work on github and merge the progress
    #try to save all uuids to csv / text file - cache


    # Unit testing needs to be included - news/test/testing


def basicNews(self):

    str1 = "top-headlines"

    fetching.fecthingfuncToo(query=str1)

    allData = NewsArticle.objects.all()

    return render(self,'news/news_by_genre.html', {'articles' : allData})


def genreNews(self, category):

    fetching.fecthingfuncToo(query=category)

    allData = NewsArticle.objects.filter(genre = category)

    return render(self,'news/news_by_genre.html', {'articles' : allData})