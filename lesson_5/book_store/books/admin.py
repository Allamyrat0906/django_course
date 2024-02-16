from django.contrib import admin

from books.models import Book, Author


class ModelAuthor(admin.ModelAdmin):
    list_display = ["id", "name", "surname"]


class ModelBook(admin.ModelAdmin):
    list_display = ["id", "title", "year", "pages","subject","author"]


# Register your models here.
admin.site.register(Book, ModelBook)
admin.site.register(Author, ModelAuthor)
