from django.db import models
from django.contrib.auth.models import User
from basic.models import Channel
from django.contrib.auth.hashers import check_password
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=50, null=True)
    otp = models.CharField(max_length=191, null=True)
    location = models.CharField(max_length=191, null=True)
    location_coordinates = models.CharField(max_length=191, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, default=1)
    ip_address = models.CharField(max_length=30, null=True)
    user_agent = models.CharField(max_length=191, null=True)
    apn_token = models.CharField(max_length=191, null=True)
    gcm_token = models.CharField(max_length=191, null=True)
    mac_address = models.CharField(max_length=191, null=True)
    avatar = models.CharField(max_length=191, null=True)
    birth_date = models.DateField(null=True)
    otp_sent_at = models.DateTimeField(null=True)
    mobile_number_verified_at = models.DateTimeField(null=True)
    mobile_number_verified = models.BooleanField(default=False)
    activation_link = models.CharField(max_length=255,null=True)
    activation_link_sent_at = models.DateTimeField(null=True)
    signed_up_with = models.CharField(max_length=30, default="email")
    banned = models.BooleanField(default=False)
    banned_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        user = self.user
        return user.first_name + user.last_name

    def check_otp(self, otp):
        return check_password(otp, self.otp)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
