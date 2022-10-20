from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomUserCreationForm

from accounts.models import User

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
        }
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
        auth_logout(request)
        return redirect("accounts:accounts")
    return render(request, "accounts/detail.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def password_update(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # update_session_auth_hash(request, form.user)
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password.html", context)
