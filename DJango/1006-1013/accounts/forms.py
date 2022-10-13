from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = get_user_model()
        fields = ("username", "email")
