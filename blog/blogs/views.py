from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Post
from .forms import PostForm


def index(request):
    """Home page."""
    blog = Blog.objects.get(id=1)
    posts = blog.post_set.order_by("-date_added")
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)


@login_required
def new_post(request):
    """Create a new post"""
    blog = Blog.objects.get(id=1)

    if request.method != "POST":
        # No data submitted, create a blank form.
        form = PostForm()
    else:
        # POST data submitted, process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.owner = request.user
            new_post.save()
            return redirect("blogs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)


@login_required
def edit_post(request, post_id):
    """Edit existing post."""
    post = Post.objects.get(id=post_id)
    check_owner_post(post.owner, request.user)

    if request.method != "POST":
        # No data submitted, create form w/ post data.
        form = PostForm(instance=post)
    else:
        # POST data received; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"post": post, "form": form}
    return render(request, "blogs/edit_post.html", context)


def check_owner_post(owner, user):
    if owner != user:
        raise Http404
