from django.shortcuts import render


def index(request):
    """The home page for pizzeria."""
    return render(request, "pizzeria/index.html")
