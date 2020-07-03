from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse # TODO: Remove this after all the HttpResponse has been modified
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', { 'latest_question_list': latest_question_list })

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the result of Question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You are voting on Question %s" % question_id)