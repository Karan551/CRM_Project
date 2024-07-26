from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="User Name",
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={
            "class": "form-control fs-4 mb-4",
            "placeholder": "Enter User Name....",
            "autocomplete": "username",
        }))

    first_name = forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(attrs={
            "class": "form-control fs-4 mb-4",
            "placeholder": "Enter Your First Name....",
        }))

    last_name = forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(attrs={
            "class": "form-control fs-4 mb-4",
            "placeholder": "Enter Your Last Name...."
        }))

    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control fs-4 mb-4",
            "placeholder": "Enter Your Email...."
        }))

    password1 = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control mb-4 fs-4",
            "placeholder": "Enter Your Password....",
            "autocomplete": "new-password",
        }))

    password2 = forms.CharField(
        label="Confirm Your Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control mb-4 fs-4",
            "placeholder": "Confirm Your Password....",
            "autocomplete": "new-password",

        }))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
