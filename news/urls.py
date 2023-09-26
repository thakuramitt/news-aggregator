from django.urls import path
from . import views

urlpatterns = [
    path('', views.basicNews, name='random_news'),
    path('<str:category>/', views.genreNews, name='sports_news'),
]