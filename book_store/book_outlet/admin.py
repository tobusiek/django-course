from django.contrib import admin

from book_outlet.models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # cannot be set with the line below
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book, BookAdmin)
