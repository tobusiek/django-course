from django import views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from reviews.forms import ReviewForm

# Create your views here.


class ReviewView(views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "reviews/review.html", {"form": ReviewForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/thank-you")

        return render(request, "reviews/review.html", {"form": form})


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, "reviews/thank_you.html")
