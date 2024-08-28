from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from django.http import HttpResponse
from .models import Record


# Create your views here.
def index(request):
    records = Record.objects.all().order_by("created_at")
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
        return render(request, "website/index.html", {"records": records})


def user_logout(request):
    logout(request)
    messages.success(request, "You're Successfully Logged Out.")
    return redirect("home")


def user_register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
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


def user_record(request, user_id):
    if request.user.is_authenticated:
        user_information = get_object_or_404(Record, pk=user_id)
        # print("this is user information", user_information)
        return render(request, "website/record.html", {"user_record": user_information})
    else:
        messages.error(request, "Please Login First To See Information.")
        return redirect("home")


def delete_record(request, user_id):
    if request.user.is_authenticated:
        customer = get_object_or_404(Record, pk=user_id)
        customer.delete()
        messages.success(request, "Record Deleted Successfully .")
        return redirect("home")
    else:
        messages.error(request, "Please Login First To Delete Record.")
        return redirect("home")


def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully.")
                return redirect("home")
        else:
            form = AddRecordForm()
        return render(request, "website/add_record.html", {"form": form})
    else:
        messages.error(request, "Please Login First To Add Record.")
        return redirect("home")


def update_record(request, user_id):
    if request.user.is_authenticated:
        current_user = get_object_or_404(Record, pk=user_id)
        if request.method == "POST":
            form = AddRecordForm(request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated Successfully.")
                return redirect("home")
        else:
            form = AddRecordForm(instance=current_user)
            return render(request, "website/update_record.html", {"form": form})
    else:
        messages.error(request, "Please Login First To Update Record.")
        return redirect("home")
