"""defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Create a new post
    path("new_post/", views.new_post, name="new_post"),
    # Edit a post
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
]
