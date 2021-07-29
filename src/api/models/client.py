from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from core.models.base import BaseModel
from core.models.extra import ConfirmCode
from django.conf import settings
from .geo import Country, City
from .user import User


class Gender(DjangoChoices):
    male = ChoiceItem("Мужчина")
    female = ChoiceItem("Женщина")


class Client(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(null=True, blank=True)
    religion = models.CharField(max_length=50, null=True)
    birth = models.DateField(null=True, blank=True)
    sex = models.CharField(choices=Gender.choices, default=Gender.male, max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100)
    confirm_code = models.OneToOneField(
        ConfirmCode, default=None, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.email


class ClientFeedBack(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email
