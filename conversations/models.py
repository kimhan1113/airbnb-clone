from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from users.models import User


class Conversation(TimeStampedModel):
    participants = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return str(self.created_at)


class Message(TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.message}'