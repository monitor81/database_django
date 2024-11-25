# books/models.py

from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pages = models.IntegerField()
    publication_year = models.IntegerField()

    def __str__(self):
        return f'{self.author} {self.title} {self.pages} {self.publication_year} '
    
    def get():
        return Book.objects.all()
