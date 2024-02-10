from typing import Any
from django.http import HttpResponse

from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form: ReviewForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)

    # def get(self, request: HttpRequest) -> HttpResponse:
    #     return render(request, "reviews/review.html", {"form": ReviewForm()})
    #
    # def post(self, request: HttpRequest) -> HttpResponse:
    #     form = ReviewForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return redirect("/thank-you")
    #
    #     return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "this works"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):  # noqa
    #     return super().get_queryset().filter(rating__gt=3)  # type: ignore


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
