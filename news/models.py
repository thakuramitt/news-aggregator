from django.db import models

# Create your models here.

class NewsArticle(models.Model):


    uuid = models.CharField(primary_key=True, max_length=10)
    genre = models.CharField(max_length=5)
    title = models.CharField(max_length=5)
    author = models.CharField(max_length=20, blank = True, null = True)
    description = models.CharField(max_length=20, blank = True, null = True)
    url = models.URLField()
    genre = models.CharField(max_length=50)
    publishedAt = models.DateTimeField(auto_now_add=True)
    urlToImage = models.CharField( max_length=100, blank = True, null = True)



    def __str__(self):
        return self.title
