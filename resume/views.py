from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
# from .forms import NewResumeForm
from .models import Resume


# Create your views here.


class ResumeView(View):
    def get(self, request):
        return render(request, 'resume/resumes.html', context={'resumes': Resume.objects.all()})
