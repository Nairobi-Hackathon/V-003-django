from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ComplianceTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='Pending')
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Notification(models.Model):
    message = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
