from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # pass
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {'fields': ('avatar','bio', 'gender', 'birthdate', 'language', 'currency', 'superhost')}),
    )