from django.contrib import admin

from book_outlet.models import Author, Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # cannot be set with the line below
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
