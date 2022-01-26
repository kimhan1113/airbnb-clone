from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from rooms.models import Room, RoomType, Facility, Amenity, HouseRule, Photo


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(ModelAdmin):
    pass







@admin.register(Room)
class RoomAdmin(ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    pass