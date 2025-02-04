from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Author, Book, BookInstance, Genre


def index(request):
    # suskaičiuojam autorius, knygas, knygų egzempliorius
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_book_instances = BookInstance.objects.count()

    context_my = {'num_authors_t': num_authors,
                  'num_books_t': num_books,
                  'num_book_instances_t': num_book_instances,}

    return render(request, 'index.html', context=context_my)
