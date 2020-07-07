from django.urls import path

from . import views

# namespace for tweet_tweet project
app_name = 'tweet_tweet'
urlpatterns = [
    # ex: '/'
    path('', views.index, name='index'),
    # ex: 'tweets/1/'
    path('tweets/<int:tweet_id>/', views.tweet_detail_view, name='detail'),
    # ex: 'tweets/'
    path('tweets/', views.tweet_list_view, name='list'),
    # ex: 'tweets/create/'
    path('tweets/create/', views.tweet_create_view, name='create')
]