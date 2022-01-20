from django.urls import path
from .views import VacancyView, NewVacancyView, MyVacancies

urlpatterns = [
    path('', VacancyView.as_view()),
    path('new', NewVacancyView.as_view()),
    path('my_vacancies', MyVacancies.as_view()),

]