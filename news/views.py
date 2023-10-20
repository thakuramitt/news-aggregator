from django.shortcuts import render
from .models import NewsArticle
from . import fetching 
import logging
logging.basicConfig(filename='logs/newsapplogs.log',
                    level=10,
                    format="{asctime}:{levelname}:{process}:{message}",
                    style='{'
                    )
def basicNews(self):
    logging.info("basic news views called")
    str1 = "top-headlines"

    fetching.fecthingfuncToo(query=str1)

    allData = NewsArticle.objects.all()
    # print("this is length of DB",len(allData))

    
    logging.info("basic news ends succesfully")
    return render(self,'news/news_by_genre.html', {'articles' : allData})

def genreNews(self, category):
    logging.info("genreNews views start")
    fetching.fecthingfuncToo(query=category)

    allData = NewsArticle.objects.filter(genre = category)
    logging.info("GenreNews views ends succesfully")
    return render(self,'news/news_by_genre.html', {'articles' : allData})
    