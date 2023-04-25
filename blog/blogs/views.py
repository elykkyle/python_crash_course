from django.shortcuts import render, redirect

from .models import Blog, Post
from .forms import PostForm


def index(request):
    """Home page."""
    blog = Blog.objects.get(id=1)
    posts = blog.post_set.order_by("-date_added")
    context = {"posts": posts}
    return render(request, "blogs/index.html", context)


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
            new_post.save()
            return redirect("blogs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)


def edit_post(request, post_id):
    """Edit existing post."""
    post = Post.objects.get(id=post_id)

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
