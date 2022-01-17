from django.urls import path
from .views import ResumeView, NewResumeView
#
urlpatterns = [
    path('', ResumeView.as_view()),
    path('new', NewResumeView.as_view()),
]