from django.db import models


class Blog(models.Model):
    """Overall model for blog"""

    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Post(models.Model):
    """A single post."""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representing the blog post."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title
