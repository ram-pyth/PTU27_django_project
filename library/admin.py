from django.contrib import admin
from .models import Author, Book, BookInstance, Genre


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # automatiškai kuriamų papildomų eilučių skaičius


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genres')
    search_fields = ('title', 'author__last_name')  # FK__tėvinėslaukas
    inlines = (BookInstanceInline,)


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'due_back', 'status')
    list_filter = ('status', 'due_back')
    search_fields = ('id', 'book__title', 'book__author__last_name')  # FK__FK__laukas
    list_editable = ('due_back', 'status')

    fieldsets = (
        ('Knyga', {'fields': ['book']}),
        ('Prieinamumas', {'fields': ['status', 'due_back']})
    )


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)


