from django.urls import path
from . import views

app_name = "practices"

urlpatterns = [
    path("index/", views.index),
    path("ping/", views.ping),
    path("pong/", views.pong),
]
