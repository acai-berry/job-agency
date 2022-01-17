from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
# from .forms import NewVacancyForm
from .models import Vacancy



class VacancyView(View):
    def get(self, request):
        return render(request, 'vacancy/vacancies.html', context={'vacancies': Vacancy.objects.all()})