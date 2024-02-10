from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def full_name(self) -> str:
        return self.first_name + " " + self.last_name

    def __str__(self) -> str:
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
