from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from basic.models import Channel
from django.contrib.auth.hashers import check_password
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mongoengine import Document, fields

# Create your models here.


class User(AbstractUser):
    mobile_number = models.CharField(max_length=30, null=True)
    otp = models.CharField(max_length=191, null=True)
    otp_sent_at = models.DateTimeField(null=True)
    mobile_number_verified_at = models.DateTimeField(null=True)
    mobile_number_verified = models.BooleanField(default=False)
    activation_link = models.CharField(max_length=191, null=True)
    activation_link_sent_at = models.DateTimeField(null=True)
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True)
    signed_up_with = models.CharField(max_length=30, default="email")
    banned = models.BooleanField(default=False)
    banned_at = models.DateTimeField(null=True)


class Profile(Document):

    #user = fields.ReferenceField('User')
    user_id = fields.IntField()
    full_name = fields.StringField(max_length=191, blank=True)
    location = fields.DictField({}, blank=True)
    settings = fields.DictField({}, blank=True)
    has_at_least_one_social_account = fields.BooleanField(default=False)
    social_accounts = fields.ListField(fields.DictField({}, blank=True), blank=True)
    associated_platforms = fields.ListField(fields.DictField(), blank=True)
    channels = fields.ListField(fields.DictField(blank=True), blank=True)
    authorized_devices = fields.ListField(fields.DictField(blank=True), blank=True)
    birth_date = fields.DateTimeField(blank=True)
    roles = fields.ListField(fields.DictField({}, blank=True), blank=True)
    permissions = fields.ListField(fields.DictField({}, blank=True), blank=True)
    signed_up_with = fields.StringField(defalut="email")
    signed_up_ip_address = fields.StringField(blank=True)
    singed_up_user_agent = fields.StringField(blank=True)
    logged_in_ip_address = fields.StringField(blank=True)
    logged_in_user_agent = fields.StringField(blank=True)


    meta = {"collection": "auth_profile"}

    def __str__(self):
        return self.mobile_number

    def check_otp(self, otp):
        return check_password(otp, self.otp)

