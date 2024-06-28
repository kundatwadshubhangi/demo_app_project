from django.db import models


# Create your models here.

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    status_message = models.CharField(max_length=255)

