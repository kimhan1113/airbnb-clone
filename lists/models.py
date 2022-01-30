from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from rooms.models import Room
from users.models import User


class List(TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room, blank=True)

    def __str__(self):
        return self.name


