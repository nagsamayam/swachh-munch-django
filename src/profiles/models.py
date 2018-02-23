from django.db import models
from django.contrib.auth.models import User
from basic.models import Channel

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=50, null=True)
    otp = models.CharField(max_length=191, null=True)
    location = models.CharField(max_length=191, null=True)
    location_coordinates = models.CharField(max_length=191, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT)
    ip_address = models.CharField(max_length=30, null=True)
    user_agent = models.CharField(max_length=191, null=True)
    apn_token = models.CharField(max_length=191, null=True)
    gcm_token = models.CharField(max_length=191, null=True)
    mac_address = models.CharField(max_length=191, null=True)
    avatar = models.CharField(max_length=191, null=True)
    birth_date = models.DateField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        user = self.user
        return user.first_name + user.last_name
