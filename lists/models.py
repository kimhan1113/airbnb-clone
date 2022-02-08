from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from rooms.models import Room
from users.models import User


class List(TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, related_name="list", on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room, related_name="list", blank=True)

    def count_rooms(self):
        return self.rooms.count()

    def __str__(self):
        return self.name

    count_rooms.short_description = "Number of Rooms"

