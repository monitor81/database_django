# books/views.py

import os
from django.shortcuts import render, redirect
from .models import Book
from django.conf import settings

def book_form(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        pages = request.POST['pages']
        publication_year = request.POST['publication_year']

        # Сохранение в базу данных
        book = Book(author=author, title=title, pages=pages, publication_year=publication_year)
        book.save()

        # Сохранение в файл
        # books_dir = os.path.join(settings.BASE_DIR, 'Books')
        # if not os.path.exists(books_dir):
        #     os.makedirs(books_dir)
        
        # file_path = os.path.join(books_dir, 'books.txt')
        # with open(file_path, 'a') as file:
        #     file.write(f"{author}, {title}, {pages}, {publication_year}\n")
        
        return redirect('books:book_list')

    return render(request, 'books/book_form.html')


def book_list(request):
    books = Book.get()
    # books_dir = os.path.join(settings.BASE_DIR, 'Books')
    # file_path = os.path.join(books_dir, 'books.txt')

    # books_data = []
    # if os.path.exists(file_path):
    #     with open(file_path, 'r') as file:
    #         books_data = file.readlines()

    # return render(request, 'books/book_list.html', {'books': books_data})
    return render (request,'books/book_list.html', {'books': books})
