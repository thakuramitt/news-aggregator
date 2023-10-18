from django.db import models
import logging
logging.basicConfig(filename='newsapplogs.log',
                    level=10,
                    format="{asctime}:{levelname}:{filename}:{process}:{message}",
                    style='{'
                    )

class NewsArticle(models.Model):
    logging.info("NewsArticle model creation started")
    uuid = models.CharField(primary_key=True, max_length=10)
    genre = models.CharField(max_length=5)
    title = models.CharField(max_length=5)
    author = models.CharField(max_length=20, blank = True, null = True)
    description = models.CharField(max_length=20, blank = True, null = True)
    url = models.URLField()
    genre = models.CharField(max_length=50)
    publishedAt = models.DateTimeField(auto_now_add=True)
    urlToImage = models.CharField( max_length=100, blank = True, null = True)
    logging.info("NewsArticle model created successfully")
    def __str__(self):
        return self.title
