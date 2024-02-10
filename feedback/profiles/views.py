from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from profiles.forms import ProfileForm
from profiles.models import UserProfile

# Create your views here.


class CreateProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "profiles/create_profile.html", {"form": ProfileForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {"form": form})
