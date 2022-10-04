from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# DateTimeField를 이용할 때 한국 시간으로 출력시키기 위해
# settings.py에서 LANGUAGE_CODE 를 ko-kr로, TIME_ZONE을 Asia/Seoul로 바꿔주면 된다.
