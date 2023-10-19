from django.test import TestCase, Client
from django.urls import reverse,resolve
from news.views import basicNews, genreNews
from news import fetching
from news.models import NewsArticle
from news.uuids.generateID import generateUUIDfromString


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url_basic_news = reverse('basic_news')
        self.list_url_genre_news = reverse('genre_news', args=['sports'])
        self.article1 = NewsArticle.objects.create(
            title = 'this is test title',
            genre = 'test',
            uuid = generateUUIDfromString('this is test title'),
        )
        return super().setUp()

    def test_views_basic_news(self):
        client = Client()
        response = client.get(self.list_url_basic_news)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news_by_genre.html')
    
    def test_views_genre_news(self):
        client = Client()
        response = client.get(self.list_url_genre_news)
        self.assertEqual(response.status_code, 200)
    
        self.assertTemplateUsed(response, 'news/news_by_genre.html')
        
    # this is not work bcz response getting error 
    # def test_views_not_args(self):
    #     client = Client()
    #     response = client.errors(reverse('genre_news'))
    #     self.assertNotEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'news/news_by_genre.html')