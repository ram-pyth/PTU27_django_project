from django.contrib import admin
from .models import Author, Book, BookInstance, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genres')


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'due_back', 'status')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Knyga', {'fields': ['book']}),
        ('Prieinamumas', {'fields': ['status', 'due_back']})
    )


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)


