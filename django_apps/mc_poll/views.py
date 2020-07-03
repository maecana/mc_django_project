from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    return HttpResponse("You are looking at Question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the result of Question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You are voting on Question %s" % question_id)