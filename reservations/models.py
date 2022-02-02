from django.db import models

# Create your models here.
from django.utils import timezone

from core.models import TimeStampedModel
from rooms.models import Room
from users.models import User


class Reservation(TimeStampedModel):

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    guest = models.ForeignKey(User, related_name="reservations", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="reservations", on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    def in_progress(self):
        now = timezone.now().date()
        print(now)
        return now > self.check_in and now < self.check_out

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out


    in_progress.boolean = True
    is_finished.boolean = True