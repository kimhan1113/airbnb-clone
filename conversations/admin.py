from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from conversations.models import Conversation, Message


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ("__str__", "created_at")


@admin.register(Conversation)
class ConversationAdmin(ModelAdmin):
    list_display = ("__str__", "count_messages", "count_participants")

