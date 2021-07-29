from django.db import models

from core.models.base import BaseModel
from core.models.order import Order
from django.conf import settings


class Dispute(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    status = models.ForeignKey("DisputeStatus", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.order.id


class DisputeStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DisputeComment(BaseModel):
    dispute = models.ForeignKey(Dispute, on_delete=models.CASCADE)

    def __str__(self):
        return self.dispute.id
