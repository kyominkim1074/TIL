from django.urls import path
from . import views_ex

app_name = "articles"

urlpatterns = [
    path("", views_ex.index, name="index"),
    path("<int:pk>/", views_ex.detail, name="detail"),
    path("create/", views_ex.create, name="create"),
    path("<int:pk>/update/", views_ex.update, name="update"),
    path("<int:pk>/delete/", views_ex.delete, name="delete"),
    path('<int:pk>/comments/', views_ex.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views_ex.comments_delete, name='comments_delete'),
    path('<int:article_pk>/likes/', views_ex.likes, name="likes"),
    path("<int:article_pk>/dislikes", views_ex.dislikes, name="dislikes"),
]
