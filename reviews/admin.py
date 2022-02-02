from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(ModelAdmin):

    list_display = ('__str__', 'rating_average')