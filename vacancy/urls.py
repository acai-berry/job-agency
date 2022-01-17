from django.urls import path
from .views import VacancyView, NewVacancyView

urlpatterns = [
    path('', VacancyView.as_view()),
    path('new', NewVacancyView.as_view()),
]