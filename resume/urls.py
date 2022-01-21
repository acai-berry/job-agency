from django.urls import path
from .views import ResumeView, NewResumeView, MyResumes
#
urlpatterns = [
    path('', ResumeView.as_view(), name='resumes'),
    path('new', NewResumeView.as_view(), name='resume_new'),
    path('my_resumes', MyResumes.as_view(), name='my_resumes'),
]