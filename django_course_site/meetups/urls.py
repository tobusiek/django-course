from django.urls import path

from meetups import views

urlpatterns = [path("meetups/", views.index)]
