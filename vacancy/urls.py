from django.urls import path
from .views import VacancyView, NewVacancyView, MyVacancies

urlpatterns = [
    path('', VacancyView.as_view(), name='vacancies'),
    path('new', NewVacancyView.as_view(), name='new_vacancy'),
    path('my_vacancies', MyVacancies.as_view(), name='my_vacancies'),

]