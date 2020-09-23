from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    year = models.TextField()
    isbn = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])