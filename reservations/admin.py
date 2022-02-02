from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = [
        'room',
        'status',
        'check_in',
        'check_out',
        'guest',
        'is_finished',
        'in_progress',
    ]

    list_filter = ("status",)