from django.db import models
from django.contrib.auth.models import User
from basic.models import Channel

# Create your models here.

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=191, null=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=191, null=True)
    location_coordinates = models.CharField(max_length=191, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT)
    ip_address = models.CharField(max_length=30, null=True)
    user_agent = models.CharField(max_length=191, null=True)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField(null=True)
    recurring = models.BooleanField(default=False)
    full_day_event = models.BooleanField(default=False)
    banner = models.CharField(max_length=191,null=True)
    parent_event = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    
    def __str__(self):
        return self.title
