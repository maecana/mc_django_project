from django.urls import path

from . import views

# namespace for tweet_tweet project
app_name = 'tweet_tweet'
urlpatterns = [
    # ex: /tweet_tweet/
    path('', views.index, name='index'),
    # ex: /tweet_tweet/tweets/1/
    path('tweets/<int:tweet_id>/', views.tweet_detail_view, name='detail'),
    # ex: /tweet_tweet/
    path('tweets/', views.tweet_list_view, name='list'),
    # ex: /tweet_tweet/tweets/create/
    path('tweets/create/', views.tweet_create_view, name='create')
]