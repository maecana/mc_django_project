# python imports
import random

# django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings

# imports from Model
from .forms import FormTweet
from .models import Tweet

# GLOBAL VARIABLES
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
LOGIN_URL = settings.LOGIN_URL

# index view
# name = index
# url: '/'
def index(request, *args, **kwargs):
    return render(request, 'tweet_tweet/pages/index.html', context={}, status=200)

# tweet create view
# name = create
# url: 'tweets/create/'
def tweet_create_view(request, *args, **kwargs):
    user = request.user

    if not user.is_authenticated:
        if request.is_ajax():
            user = None
            return JsonResponse({}, status=401) # 401==Unauthorized, 403==forbidden
        return redirect(request, LOGIN_URL)

    form = FormTweet(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        
        if request.is_ajax():
            return JsonResponse(obj.serialize(),  status=201) # 201 == created items

        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)

        form = FormTweet()
    elif form.errors and request.is_ajax():
        return JsonResponse(form.errors, status=400)
    return render(request, 'tweet_tweet/components/form.html', context={'form':form})

# tweet list view
# name = list
# url: 'tweets/'
# return json data of all tweets
def tweet_list_view(request, *args, **kwargs):
    """
    REST API
    Get all Tweet objects
    return json response data
    """
    tweets = Tweet.objects.all()
    tweet_list = [tweet.serialize() for tweet in tweets]
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