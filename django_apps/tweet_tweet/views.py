import random

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Tweet

# index view
def index(request, *args, **kwargs):
    return render(request, 'tweet_tweet/pages/index.html', context={}, status=200)

# tweet list view
def tweet_list_view(request, *args, **kwargs):
    """
    REST API
    Consumed by Javascript
    return JSON data
    """
    tweets = Tweet.objects.all()
    tweet_list = [{'id': tweet.id, 'content': tweet.content, 'likes': random.randint(0, 122)} for tweet in tweets]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)

# API for getting detail of a tweet
# parameter: <int: tweet_id>
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API
    Consume by Javascript
    return JSON data
    """
    data = {
        'id': tweet_id
    }
    status = 200

    try:
        tweet = get_object_or_404(Tweet, pk=tweet_id)
        data['content'] = tweet.content
    except:
        data['message'] = '404 Not Found'
        status = 404
    
    return JsonResponse(data, status=status)