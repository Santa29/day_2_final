from django.urls import path
from .views import HomePageView, AboutPageView, ContactsPageView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('contacts/', ContactsPageView.as_view(), name  = 'contacts'),
    path('books/new/', BookCreateView.as_view(), name = 'book_new'),
    path('books/<int:pk>/', BookDetailView.as_view(), name = 'book_detail'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name = 'book_edit'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name = 'book_delete')
]