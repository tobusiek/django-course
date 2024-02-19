from django.contrib import admin

from meetups.models import Location, Meetup, Participant

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    list_filter = ("title", "location", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
