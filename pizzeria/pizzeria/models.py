from django.db import models


class Pizza(models.Model):
    """A type of pizza."""

    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the name of the pizza."""
        return self.name.title()


class Topping(models.Model):
    """A specific topping for the pizza."""

    name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the name of the topping."""
        return self.name
