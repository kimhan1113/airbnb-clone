from django.db import models

# Create your models here.
#
from django_countries.fields import CountryField

from core.models import TimeStampedModel
from users.models import User


class AbstractItem(TimeStampedModel):


    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"
        ordering = ['-updated_at']

class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"

    pass

class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"
    pass


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(TimeStampedModel):
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    cehck_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name