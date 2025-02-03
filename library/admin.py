from django.contrib import admin
from .models import Author, Book, BookInstance, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genres')


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance)
admin.site.register(Genre)


