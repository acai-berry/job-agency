from django.urls import path
from .views import ResumeView, NewResumeView, MyResumes
#
urlpatterns = [
    path('', ResumeView.as_view()),
    path('new', NewResumeView.as_view()),
    path('my_resumes', MyResumes.as_view()),
]