from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Book

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Book
    context_object_name = 'books_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'