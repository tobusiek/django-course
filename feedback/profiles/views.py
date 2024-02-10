import os
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


def store_file(file: UploadedFile) -> None:
    with open(os.path.join(os.getcwd(), "temp", file.name), "wb+") as image_file:
        for chunk in file.chunks():
            image_file.write(chunk)


class CreateProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "profiles/create_profile.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
