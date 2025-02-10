from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q  # Q - kombinuoti keletą filtravimo sąlygų su OR
from django.core.paginator import Paginator  # funkcijų puslapiavimui
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Author, Book, BookInstance, Genre


def index(request):
    # suskaičiuojam autorius, knygas, knygų egzempliorius
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_book_instances = BookInstance.objects.count()

    # knygų egz su statusu g(galima paimti) skaičius
    num_book_insts_available = BookInstance.objects.filter(status__exact='g').count()

    # skaitliukas anoniminiams useriams
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context_my = {'num_authors_t': num_authors,
                  'num_books_t': num_books,
                  'num_book_instances_t': num_book_instances,
                  'num_book_insts_available_t': num_book_insts_available,
                  'num_visits_t': num_visits
                  }

    return render(request, 'index.html', context=context_my)


def get_authors(request):
    # visos eilutės iš author lentelės
    authors = Author.objects.all()
    paginator = Paginator(authors, 3)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    context = {'authors': paged_authors}
    return render(request, 'authors.html', context=context)


def get_one_author(request, author_id):
    # author_id - integer, pagal jį ieškom author lentelėj eilutės
    one_author = get_object_or_404(Author, pk=author_id)
    context = {'one_author': one_author}
    return render(request, 'author.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # book_list - standartinis kintamojo template pavadinimas,sukuriamas django
    template_name = 'books.html'
    paginate_by = 8  # templeite sukuriamas page_obj


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'  # book - standartinis kintamojo template pavadinimas,sukuriamas django
    template_name = 'book.html'


def search(request):
    # request.GET - žodynas su requesto params
    query_text = request.GET.get('search_text')
    # https://docs.djangoproject.com/en/4.2/ref/models/lookups/
    search_results = Book.objects.filter(
        Q(title__icontains=query_text)
        | Q(author__last_name__icontains=query_text)
        | Q(summary__icontains=query_text)
    )

    context = {'query_text': query_text,
               'book_list': search_results}

    return render(request, 'search_results.html', context=context)


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    context_object_name = 'bookinstance_list'
    template_name = 'user_books.html'

    def get_queryset(self):
        return BookInstance.objects.filter(reader=self.request.user)
