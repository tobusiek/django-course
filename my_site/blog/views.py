from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from blog.forms import CommentForm
from blog.models import Post

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):  # noqa
        return super().get_queryset()[:3]


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page"), args=[slug])

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
        }
        return render(request, "blog/post-detail.html", context)
