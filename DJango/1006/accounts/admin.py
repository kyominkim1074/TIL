from django.contrib import admin
from django.contrib.auth import Useradmin
from .models import User

# Register your models here.

admin.site.register(User, Useradmin)
