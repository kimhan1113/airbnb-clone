from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from lists.models import List


@admin.register(List)
class ListAdmin(ModelAdmin):
    pass