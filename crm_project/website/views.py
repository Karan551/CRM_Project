from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
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
