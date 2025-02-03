"""
DĖMESIO
šis kodas vykdomas per copy paste į Django Shell,
iškviečiamą terminale - python manage.py shell

papildom knygų kopijomis biblioteką
"""
from library.models import Book, BookInstance
import random

books = Book.objects.all()
book_instances = []
for book in books:
    rand_number_of_instances = random.randint(5, 8)
    for _ in range(rand_number_of_instances):
        BookInstance.objects.create(book=book)
