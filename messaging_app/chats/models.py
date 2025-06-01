from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class User(AbstractUser):
    user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        Group,
        related_name="chats_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="chats_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    participants = models.ManyToManyField(User)

class Message(models.Model):
    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    message_body = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        ordering = ["created_at"]
