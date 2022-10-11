from django.shortcuts import render, redirect

from accounts.models import User

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)


def accounts(request):
    accounts = User.objects.order_by("pk")
    context = {
        "accounts": accounts,
    }
    return render(request, "accounts/accounts.html", context)


def delete(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("accounts:accounts")
    return render(request, "accounts/detail.html")
