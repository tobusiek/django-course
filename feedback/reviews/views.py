from typing import Any

from django import views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from reviews.forms import ReviewForm
from reviews.models import Review

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


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "this works"
        return context


class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Review.objects.get(pk=review_id)
        context["review"] = review
        return context
