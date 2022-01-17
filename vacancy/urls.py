from django.urls import path
from .views import VacancyView

urlpatterns = [
    path('', VacancyView.as_view()),
]