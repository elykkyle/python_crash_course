from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        labels = {"title": "title", "text": "text"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
