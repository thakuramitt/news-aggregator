from django.shortcuts import render
from .models import NewsArticle
from . import fetching 
import logging
logger = logging.getLogger(__name__)

def basicNews(self):
    try:
        logger.info("basic news views called")
        str1 = "top-headlines"

        fetching.fecthingfuncToo(query=str1)
        logger.info("fetching function run succesfully")

        allData = NewsArticle.objects.all()
        # print("this is length of DB",len(allData))
        logger.info("basic news ends succesfully")
        return render(self,'news/news_by_genre.html', {'articles' : allData})
    except Exception as obj:
        logger.exception("exception",obj)
def genreNews(self, category):
    try:
        logger.info("genreNews views start")
        
        fetching.fecthingfuncToo(query=category)
        logger.info("fetching function run succesfully")

        allData = NewsArticle.objects.filter(genre = category)
        logger.info("GenreNews views ends succesfully")
        return render(self,'news/news_by_genre.html', {'articles' : allData})
    except Exception as obj:
        logger.exception("exception",obj)
    