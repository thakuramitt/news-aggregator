from django.test import SimpleTestCase
from django.urls import reverse,resolve
from news.views import basicNews, genreNews

class TestUrls(SimpleTestCase):
    def test_basic_news(self):
        url = reverse('basic_news')
        self.assertEqual(resolve(url).func, basicNews)
        
    def test_genreNews(self):
        url = reverse('genre_news', args=['news'])
        self.assertEqual(resolve(url).func, genreNews)
