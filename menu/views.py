from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from vacancy.forms import NewVacancyForm
from resume.forms import NewResumeForm

# Create your views here.


class MenuView(View):
    def get(self, request, *args, **kwargs):
        form = NewVacancyForm() if request.user.is_staff else NewResumeForm()
        context = {
            'form': form,
            'is_authenticated': request.user.is_authenticated,
            'is_staff': request.user.is_staff,
            'username': request.user.username,
        }
        return render(request, 'menu/home.html', context=context)


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/login.html'