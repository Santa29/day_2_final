from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignUpView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm