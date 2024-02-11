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
    def is_stored_post(self, request: HttpRequest, post_id: int) -> bool:
        stored_posts = request.session.get("stored_posts")
        return post_id in stored_posts if stored_posts is not None else False

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),  # type: ignore
            "saved_for_later": self.is_stored_post(request, post.id),
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),  # type: ignore
            "saved_for_later": self.is_stored_post(request, post.id),
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        stored_posts = request.session.get("stored_posts", [])

        context = {}
        if len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request: HttpRequest) -> HttpResponse:
        stored_posts = request.session.get("stored_posts", [])
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
