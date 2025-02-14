from rest_framework import viewsets, generics

from library.models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookSearchListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        book_title = self.request.query_params.get('book', None)
        author_name = self.request.query_params.get('author', None)

        if book_title:
            queryset = queryset.filter(title__icontains=book_title)
        if author_name:
            queryset = queryset.filter(author__last_name__icontains=author_name)
        return queryset

# paieškos su 2 param pvz
# /api/books/search/?book=py&author=lutz


