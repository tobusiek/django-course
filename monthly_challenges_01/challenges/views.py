from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

MONTHLY_CHALLENGES: dict[str, str] = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Eat no meat for the entire month!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Eat no meat for the entire month!",
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

    return render(
        request,
        "challenges/challenge.html",
        {"month": month, "challenge": MONTHLY_CHALLENGES[month]},
    )
