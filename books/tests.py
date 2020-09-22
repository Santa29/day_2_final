from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.
class PostModelTests(TestCase):
    def setUp(self):
        Book.objects.create(title = 'title', author = 'author', year = 'year', isbn = 'isbn')

    def test_content(self):
        current_post = Book.objects.get(id=1)
        expected_title = current_post.title
        expected_author = current_post.author
        expected_year = current_post.year
        expected_isbn = current_post.isbn

        self.assertEqual(expected_title, 'title')
        self.assertEqual(expected_author, 'author')
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

class ContactsPageViewTest(TestCase):
    def setUp(self):
        Book.objects.create(title = 'title', author = 'author', year = 'year', isbn = 'isbn')

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