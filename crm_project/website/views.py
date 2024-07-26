from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect("home")
        else:
            messages.error(request, "There was an error UserName or Password.")
            return redirect("home")

    else:
        return render(request, "website/index.html")


def user_logout(request):
    logout(request)
    messages.success(request, "You're Successfully Logged Out.")
    return redirect("home")


def user_register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # print(form.errors)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "website/register.html", {"form": form})

    # return render(request, "website/register.html", {"form": form})
