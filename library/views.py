from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Q  # Q - kombinuoti keletą filtravimo sąlygų su OR
from django.core.paginator import Paginator  # funkcijų puslapiavimui
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Author, Book, BookInstance, User
from .utils import check_pasword


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


def register_user(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')

    elif request.method == 'POST':
        # paimam duomenis iš formos
        # request.POST - žodynas
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not check_pasword(password):
            messages.error(request, 'Slaptažodis, mažiausiai 5 simboliai!!!')
            return redirect('register')

        if password != password2:
            messages.error(request, 'Slaptažodžiai nesutampa')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, f'Vartotojo vardas {username} jau užimtas')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, f'Email {email} jau užregistruotas')
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password)
        messages.info(request, f'Vartotojas {username} užregistruotas!')
        return redirect('login')
