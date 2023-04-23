from django.db import models
from common.models import CommonModel


# Create your models here.
class ChatRoom(CommonModel):
    # Room Model Definition
    users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "Chat Room"


class Message(CommonModel):
    # Message model definition
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} says {self.text}"
