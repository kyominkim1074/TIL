from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("accounts/<int:pk>/", views.detail, name="detail"),
    path("accounts/", views.accounts, name="accounts"),
    path("accounts/<int:pk>/delete", views.delete, name="delete"),
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("accounts/update/", views.update, name="update"),
    path("accounts/password/", views.password_update, name="password"),
    path("<int:pk>/follow/", views.follow, name="follow"),
]
