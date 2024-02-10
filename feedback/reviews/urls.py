from django.urls import path

from reviews import views

urlpatterns = [
    path("", views.review),
    path("thank-you", views.thank_you),
]
