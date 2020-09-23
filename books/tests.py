from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book

# Create your tests here.
class bookModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "testuser",
            password = "123456",
            email = "test@email.com",
        )

        self.book = Book.objects.create(title = 'title', author = self.user, year = 'year', isbn = 'isbn')

    def test_content(self):
        current_book = Book.objects.get(id=1)
        expected_title = current_book.title
        expected_author = current_book.author
        expected_year = current_book.year
        expected_isbn = current_book.isbn

        self.assertEqual(expected_title, 'title')
        self.assertEqual(expected_author, 'testuser')
        self.assertEqual(expected_year, 'year')
        self.assertEqual(expected_isbn, 'isbn')


class HomePageViewTest(TestCase):
    def setUp(self):
        Book.objects.create(title = 'title', author = 'author', year = 'year', isbn = 'isbn')

    def test_view_url_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class AboutPageViewTest(TestCase):
    def setUp(self):
        Book.objects.create(title = 'title', author = 'author', year = 'year', isbn = 'isbn')

    def test_view_url_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class BookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "testuser",
            password = "123456",
            email = "test@email.com",
        )

        self.book = Book.objects.create(title = 'title', author = self.user, year = 'year', isbn = 'isbn')

    def test_view_url_status_code(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')

    def test_str_representation(self):
        book = Book(title='Sample title')
        self.assertEqual(str(book), book.title)
    
    def test_book_content_in_db(self):
        self.assertEqual(self.book.title, "title")
        self.assertEqual(self.book.year, "year")
        self.assertEqual(self.book.isbn, "isbn")
        self.assertEqual(str(self.book.author), 'testuser')

    def test_book_list_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_book_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_book_list_view_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title")

    def test_detail_view_valid(self):
        response = self.client.get('/book/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')
        self.assertContains(response, "title")

    def test_detail_view_invalid(self):
        response = self.client.get('/book/10000000/')
        self.assertEqual(response.status_code, 404)
    
    def test_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), '/books/1/')

    def test_book_create_view(self):
        response = self.client.post(reverse('book_new'), {
            'title': "New title",
            "year": "year",
            'author': "self.user",
            'isbn': "isbn"
            })
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, "New title")
        self.assertContains(response, "year")
        self.assertContains(response, "isbn")
        self.assertTemplateUsed(response, 'book_new.html')

    def test_book_update_view(self):
        response = self.client.book(reverse('book_edit', args='1'), {
            'year' : 'Updated year',
            'isbn' : 'Updated isbn',
        })
        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, 'book_edit.html')

    def test_book_delete_view(self):
        response = self.client.get(
            reverse('book_delete', args='1')
        )
        self.assertEqual(response.status_code, 200)