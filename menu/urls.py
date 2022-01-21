from django.urls import path
from .views import MenuView, MyLoginView, MySignupView
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view()),
    path('signup', MySignupView.as_view(), name='signup'),
    ]