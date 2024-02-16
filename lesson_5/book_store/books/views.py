from django.shortcuts import render
from .models import Book
# Create your views here.


def all_books(request):
    all_book = Book.objects.all()
    return render(request, "books/all_books.html", {
        "books": all_book
    })


def book_detail(request, id):
    book_detail = Book.objects.get(pk=id)
    return render(request, "books/book_detail.html", {
        "book_detail": book_detail
    })
