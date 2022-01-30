from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from conversations.models import Conversation, Message


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    pass


@admin.register(Conversation)
class ConversationAdmin(ModelAdmin):
    pass

