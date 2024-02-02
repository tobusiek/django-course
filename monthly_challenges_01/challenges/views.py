from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    challenge_text: bytes
    if month == "january":
        challenge_text = b"Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = b"Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = b"Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound(b"This month is not supported!")

    return HttpResponse(challenge_text)
