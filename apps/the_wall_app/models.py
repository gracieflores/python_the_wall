from django.db import models
from apps.login_app.models import User

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)