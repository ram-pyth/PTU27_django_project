from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_nm'),
    path('authors/', views.get_authors, name='authors-all'),
    path('authors/<int:author_id>', views.get_one_author, name='author-one'),
    path('books/', views.BookListView.as_view(), name='books-all'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-one'),
    path('search/', views.search, name='search_nm'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-books'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.get_user_profile, name='user-profile'),
    path('mybooks/new', views.BookInstanceByUserCreateView.as_view(), name='my-borrowed-new'),
]
