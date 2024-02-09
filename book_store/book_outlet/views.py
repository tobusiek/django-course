from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
