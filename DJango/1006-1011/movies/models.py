from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=20, verbose_name="제목")
    summary = models.TextField(verbose_name="줄거리")
    running_time = models.IntegerField(verbose_name="러닝타임")
