from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    pass