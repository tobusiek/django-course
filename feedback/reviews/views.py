from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


def review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data["user_name"],
                review_text=form.cleaned_data["review_text"],
                rating=form.cleaned_data["rating"],
            )
            review.save()
            return redirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, "reviews/thank_you.html")
