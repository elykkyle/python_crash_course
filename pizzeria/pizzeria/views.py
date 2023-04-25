from django.shortcuts import render
from .models import Pizza


def index(request):
    """The home page for pizzeria."""
    return render(request, "pizzeria/index.html")


def pizzas(request):
    """Page to list all pizzas."""
    pizzas = Pizza.objects.order_by("name")
    context = {"pizzas": pizzas}
    return render(request, "pizzeria/pizzas.html", context)


def pizza(request, pizza_id):
    """Detail page for single pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("name")
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzeria/pizza.html", context)
