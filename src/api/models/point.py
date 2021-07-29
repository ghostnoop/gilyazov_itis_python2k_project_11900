from django.db import models
from core.models.base import BaseModel
from core.models.client import Client
from django.conf import settings


class Relation(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Point(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    dead_date = models.DateField()
    relation = models.ForeignKey(Relation, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    avatar = models.ImageField(null=True)

    def __str__(self):
        return f"{self.pk} {self.surname} {self.name} {self.last_name}"


class PointPhoto(BaseModel):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    photo = models.ImageField()

    def __str__(self):
        return self.point.id


class PointNotification(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    birth = models.BooleanField(default=False)
    dead = models.BooleanField(default=False)
    day_and_month_to_notify = models.DateField()

    def __str__(self):
        return f"{self.point.id} - {self.day_and_month_to_notify}"
