import random

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings

# imports from Model
from .forms import FormTweet
from .models import Tweet


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# index view
def index(request, *args, **kwargs):
    return render(request, 'tweet_tweet/pages/index.html', context={}, status=200)

# tweet create view
def tweet_create_view(request, *args, **kwargs):
    form = FormTweet(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        print(ALLOWED_HOSTS)
        print(is_safe_url(next_url, ALLOWED_HOSTS))
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = FormTweet()
    return render(request, 'tweet_tweet/components/form.html', context={'form':form})

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