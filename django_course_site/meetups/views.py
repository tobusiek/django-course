from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from meetups.models import Meetup

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    meetups = Meetup.objects.all()
    return render(
        request,
        "meetups/index.html",
        {"meetups": meetups, "show_meetups": True},
    )


def meetup_details(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        selected_meetup = Meetup.objects.get(slug=slug)
        return render(
            request,
            "meetups/meetup-details.html",
            {
                "meetup_found": True,
                "title": selected_meetup.title,
                "description": selected_meetup.description,
            },
        )
    except Exception:
        return render(
            request, "meetups/meetup-details.html", {"meetup_found": False}
        )
