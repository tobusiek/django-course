from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from meetups.forms import RegistrationForm
from meetups.models import Meetup, Participant

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    meetups = Meetup.objects.all()
    return render(
        request,
        "meetups/index.html",
        {"meetups": meetups, "show_meetups": True},
    )


def meetup_details(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        selected_meetup = Meetup.objects.get(slug=slug)
        if request.method == "GET":
            form = RegistrationForm()
        else:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                participant_email = form.cleaned_data["email"]
                participant, was_created = Participant.objects.get_or_create(
                    email=participant_email
                )
                selected_meetup.participants.add(participant)
                return redirect("confirm-registration")
        return render(
            request,
            "meetups/meetup-details.html",
            {
                "meetup_found": True,
                "meetup": selected_meetup,
                "form": form,
            },
        )
    except Exception:
        return render(
            request, "meetups/meetup-details.html", {"meetup_found": False}
        )


def confirm_registration(request: HttpRequest) -> HttpResponse:
    return render(request, "meetups/registration-success.html")
