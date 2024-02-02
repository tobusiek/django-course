from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

MONTHLY_CHALLENGES: dict[str, bytes] = {
    "january": b"Eat no meat for the entire month!",
    "february": b"Walk for at least 20 minutes every day!",
    "march": b"Learn Django for at least 20 minutes every day!",
    "april": b"Eat no meat for the entire month!",
    "may": b"Walk for at least 20 minutes every day!",
    "june": b"Learn Django for at least 20 minutes every day!",
    "july": b"Eat no meat for the entire month!",
    "august": b"Walk for at least 20 minutes every day!",
    "september": b"Eat no meat for the entire month!",
    "october": b"Eat no meat for the entire month!",
    "november": b"Walk for at least 20 minutes every day!",
    "december": b"Eat no meat for the entire month!",
}

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    list_months = "<ol>"

    for month in MONTHLY_CHALLENGES:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_months += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    return HttpResponse(f"{list_months}</ol>".encode())


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    months = list(MONTHLY_CHALLENGES.keys())

    if month > len(months):
        return HttpResponseNotFound(b"<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    if month not in MONTHLY_CHALLENGES:
        return HttpResponseNotFound(b"<h1>Wrong month spelling!</h1>")

    response_data = render_to_string("challenges/challenge.html")
    return HttpResponse(response_data)
    # return HttpResponse(f"<h1>{MONTHLY_CHALLENGES[month]}</h1>".encode())
