from django.urls import path

from meetups import views

urlpatterns = [
    path("meetups", views.index, name="all-meetups"),
    path(
        "meetups/<slug:slug>/success",
        views.confirm_registration,
        name="confirm-registration",
    ),
    path("meetups/<slug:slug>", views.meetup_details, name="meetup-details"),
]
