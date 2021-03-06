from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from rooms.models import Room
from users.models import User


class Review(TimeStampedModel):
    review = models.TextField()
    accuracy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    communication = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cleanliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    location = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    check_in = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review}-{self.room}'

    def rating_average(self):
        avg = (
            self.accuracy +
            self.communication +
            self.cleanliness +
            self.location +
            self.check_in +
            self.value
        ) / 6

        return round(avg,2)

    rating_average.short_description = "Avg"

    class Meta:
        ordering = ("-created_at",)
