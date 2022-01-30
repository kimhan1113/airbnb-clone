from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from users.models import User


class List(TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

