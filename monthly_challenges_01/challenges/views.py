from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseNotFound
from django.shortcuts import render

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


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    return HttpResponse(bytes(month))


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    if month not in MONTHLY_CHALLENGES:
        return HttpResponseNotFound(b"Wrong month spelling!")

    return HttpResponse(MONTHLY_CHALLENGES[month])
