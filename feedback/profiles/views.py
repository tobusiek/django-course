from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


class CreateProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "profiles/create_profile.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        print(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
