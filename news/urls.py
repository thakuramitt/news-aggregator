from django.urls import path
from . import views

urlpatterns = [
    path('', views.basicNews, name='basic_news'),
    path('<str:category>/', views.genreNews, name='genre_news'),
]