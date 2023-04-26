from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # POST data received. process data.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page.
            login(request, new_user)
            return redirect("blogs:index")

    # Display blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)
