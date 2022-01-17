from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import NewVacancyForm
from .models import Vacancy



class VacancyView(View):
    def get(self, request):
        return render(request, 'vacancy/vacancies.html', context={'vacancies': Vacancy.objects.all()})


class NewVacancyView(View):
    def post(self, request, *args, **kwargs):
        can_submit = request.user.is_authenticated and request.user.is_staff
        if not can_submit:
            return HttpResponse(status=403)

        form = NewVacancyForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('<h1>400 Bad Request</h1>')

        author = request.user
        description = form.cleaned_data['description']
        Vacancy.objects.create(author=author, description=description)
        return redirect('/vacancies')