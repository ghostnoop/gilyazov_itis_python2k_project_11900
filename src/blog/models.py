from django.db import models

# Create your models here.
from core.models.base import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=200)
    text = models.TextField()
    preview = models.ImageField()


class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()


class Sources(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    link = models.URLField()
