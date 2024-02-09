from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse("book-detail", args=[self.id])  # type: ignore

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
