from django.urls import path

from meetups import views

urlpatterns = [
    path("meetups", views.index),
    path("meetups/<slug:slug>", views.meetup_details),
]
