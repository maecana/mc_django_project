from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. You are at polls index.")

def details(request, question_id):
    return HttpResponse("You are looking at Question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the result of Question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You are voting on Question %s" % question_id)