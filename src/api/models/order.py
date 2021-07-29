from django.db import models
from core.models.base import BaseModel
from core.models.client import Client
from core.models.executor import Executor, Service
from core.models.point import Point
from django.conf import settings


class OrderStatus(models.Model):
    name = models.CharField(max_length=50)


class Order(BaseModel):
    executor = models.ForeignKey(Executor, on_delete=models.SET_NULL, null=True)
    point = models.ForeignKey(Point, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    order_services = models.ManyToManyField(Service)

    def __str__(self):

        return self.client.id
