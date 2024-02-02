from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def january(request: HttpRequest) -> HttpResponse:
    return HttpResponse(b"Eat no meat for an entire month!")


def february(request: HttpRequest) -> HttpResponse:
    return HttpResponse(b"Walk for at least 20 minutes every day!")


def march(request: HttpRequest) -> HttpResponse:
    return HttpResponse(b"Learn Django for at least 20 minutes every day!")
