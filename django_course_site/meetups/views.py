from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    meetups = [
        {
            "title": "A first meetup",
            "location": "New York",
            "slug": "first-meetup",
        },
        {
            "title": "A second meetup",
            "location": "Paris",
            "slug": "second-meetup",
        },
    ]
    return render(
        request,
        "meetups/index.html",
        {"meetups": meetups, "show_meetups": True},
    )
