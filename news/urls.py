from django.urls import path
from . import views

urlpatterns = [
    path('', views.basicNews, name='random_news'),
    path('sports', views.top_headlines, name='sports_news'),
    path('business', views.businessNews, name='business_news'),
    path('entertainment', views.entertainmentNews, name='entertainment_news'),
    path('health', views.healthNews, name='health_news'),
    path('science', views.scienceNews, name='science_news'),
    path('technology', views.technologyNews, name='technology_news'),
    path('us', views.usNews, name='us_news'),
    path('in', views.indiaNews, name='in_news'),
    path('bbc', views.bbcNews, name='bbc_news'),
    path('fox', views.foxNews, name='fox_news'),
]