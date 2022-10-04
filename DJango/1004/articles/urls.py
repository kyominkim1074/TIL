from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # 주소:(http://127.0.0.1:8000/articles/)
    path("", views.index, name="index"),
    # http://127.0.0.1:8000/articles/create
    path("new/", views.create, name="new"),
    # http://127.0.0.1:8000/articles/pk/
    path("<int:pk>/", views.detail, name="detail"),
    # http://127.0.0.1:8000/articles/pk/update/
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
