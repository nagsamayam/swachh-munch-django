from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from basic.models import Channel
from django.contrib.auth.hashers import check_password
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mongoengine import Document, fields


class User(AbstractUser):
    mobile_number = models.CharField(max_length=30, null=True)
    otp = models.CharField(max_length=191, null=True)
    otp_sent_at = models.DateTimeField(null=True)
    mobile_number_verified_at = models.DateTimeField(null=True)
    mobile_number_verified = models.BooleanField(default=False)
    email_activation_link = models.CharField(max_length=191, null=True)
    email_activation_link_sent_at = models.DateTimeField(null=True)
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True)
    banned = models.BooleanField(default=False)
    banned_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    def check_otp(self, plain_otp):
        return check_password(plain_otp, self.otp)

