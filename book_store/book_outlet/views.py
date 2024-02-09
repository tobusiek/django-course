from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from book_outlet.models import Book

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
        },
    )


def book_detail(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
