from .models import Article
from django.contrib import admin

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


admin.site.register(Article, ArticleAdmin)
