from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Book
    context_object_name = 'books_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_new.html'
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_edit.html'
    fields = ['year', 'isbn']

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')