from django.shortcuts import render

# Create your views here.


from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
        if user:
            login(self.request, user)
        return response

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('landing')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ProfileView(DetailView):
    pass




        
