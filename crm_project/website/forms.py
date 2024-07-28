from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

css_class = "mb-3 form-control form-control-lg fs-4 px-3"


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


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["first_name", "last_name", "contact_number", "email_address", "address", "city", "zipCode"]

        labels = {
            "first_name": "Enter First Name",
            "last_name": "Enter Last Name",
            "contact_number": "Enter Contact Number",
            "email_address": "Enter Email Address",
            "city": "Enter City Name",
            "zipCode": "Enter Zip Code",
            "address": "Enter Your Address",
        }

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "Enter First Name...",
                "class": css_class,
            }),

            "last_name": forms.TextInput(attrs={
                "placeholder": "Enter Last Name...",
                "class": css_class,
            }),

            "contact_number": forms.TextInput(attrs={
                "placeholder": "Enter Contact Number...",
                "class": css_class,
            }),

            "email_address": forms.TextInput(attrs={
                "placeholder": "Enter Your Email Address...",
                "class": css_class
            }),

            "address": forms.TextInput(attrs={
                "placeholder": "Enter Your Address...",
                "class": css_class
            }),

            "city": forms.TextInput(attrs={
                "placeholder": "Enter Your City...",
                "class": css_class
            }),

            "zipCode": forms.TextInput(attrs={
                "placeholder": "Enter Your Zip Code...",
                "class": css_class
            }),

        }
