from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Author, Book, BookInstance, Genre


def index(request):
    # suskaičiuojam autorius, knygas, knygų egzempliorius
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_book_instances = BookInstance.objects.count()

    # knygų egz su statusu g(galima paimti) skaičius
    num_book_insts_available = BookInstance.objects.filter(status__exact='g').count()

    context_my = {'num_authors_t': num_authors,
                  'num_books_t': num_books,
                  'num_book_instances_t': num_book_instances,
                  'num_book_insts_available_t': num_book_insts_available,
                  }

    return render(request, 'index.html', context=context_my)


def get_authors(request):
    # visos eilutės iš author lentelės
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors.html', context=context)
