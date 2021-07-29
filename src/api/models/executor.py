from django.db import models

from core.models.base import BaseModel
from core.models.extra import ConfirmCode
from core.models.geo import Country, City
from core.models.user import User
from django.conf import settings


class Executor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField()
    confirm_code = models.OneToOneField(
        ConfirmCode, default=None, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.email


class Service(BaseModel):
    parent = models.ForeignKey("Service", on_delete=models.CASCADE, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    describe = models.TextField()
    price = models.FloatField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
