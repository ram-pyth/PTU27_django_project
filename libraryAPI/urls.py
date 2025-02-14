from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorViewSet.as_view({'get': 'list'})),
    path('books/', views.BookListAPIView.as_view()),
]
