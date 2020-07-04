from django.urls import path

from . import views

app_name = 'mc_poll'
urlpatterns = [
    # ex: /mc_poll/
    path('', views.index, name='index'),
    # ex: /mc_poll/1
    path('<int:question_id>/', views.details, name='details'),
    # ex: /mc_poll/1/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /mc_poll/1/votes
    path('<int:question_id>/vote/', views.vote, name='vote')
]