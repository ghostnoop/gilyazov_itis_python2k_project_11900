from django.db import models

from core.models.base import BaseModel


class ConfirmCode(BaseModel):
    code = models.IntegerField(default=0)
    timeout = models.DateTimeField()
