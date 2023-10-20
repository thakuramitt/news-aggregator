from news.models import NewsArticle
from django.test import TestCase
import pytest

@pytest.mark.django_db(transaction=True)
class Testdb(TestCase):
    def setUp(self):
        print("this is test for DB ")
        NewsArticle.objects.create(
                    genre = 'test',
                    uuid = 'bc12ol34nc',
                    title='this is test article',
                    author='unknown',
                )
        print("this is test for DB ")
    
    def test_fecthingfuncToo(self):
        uuidmy = NewsArticle.objects.get(uuid = 'bc12ol34nc')
        self.assertEqual(uuidmy.uuid, 'bc12ol34nc')
        self.assertEqual(uuidmy.genre, 'test')
        self.assertEqual(uuidmy.title, 'this is test article')

    # def test_delete_data(self):
    #     uuidmy = self.arcticle.uuid
        # data delete

        # uuidmy = self.arcticle.uuid
        # data = NewsArticle.objects.get(uuid =uuidmy)
        # self.assertEquals(data.uuid, self.arcticle.uuid)
        # self.assertEquals(data.genre, self.arcticle.genre)
        # self.assertEquals(data.title, self.arcticle.title)
        # self.assertEquals(data.uuid, NewsArticle.objects.filter(genre="test"))

    # multiple articles create and test - use list compre.
    # deleting data then test