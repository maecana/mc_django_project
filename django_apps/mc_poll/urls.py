from django.urls import path

from . import views

app_name = 'mc_poll'
urlpatterns = [
    # ex: /mc_poll/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /mc_poll/1
    path('<int:pk>/', views.DetailsView.as_view(), name='details'),
    # ex: /mc_poll/1/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /mc_poll/1/votes
    path('<int:question_id>/vote/', views.vote, name='vote')
]