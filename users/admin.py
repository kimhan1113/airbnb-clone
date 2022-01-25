from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(ModelAdmin):
    pass