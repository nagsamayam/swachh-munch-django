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


class Profile(Document):

    # owner = fields.ReferenceField('User')
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
    signed_up_with = fields.StringField(default="email")
    signed_up_ip_address = fields.StringField(blank=True)
    singed_up_user_agent = fields.StringField(blank=True)
    login_in_ip_address = fields.StringField(blank=True)
    login_in_user_agent = fields.StringField(blank=True)


    meta = {"collection": "auth_profile"}

    def __str__(self):
        return self.user_id

    @property
    def user(self):
        if 'user' not in self._data:
            self._data['user'] = User.objects.get(pk=self.user_id)
        
        return self._data['user']

    @user.setter
    def user(self, value):
        if value and hasattr(value, 'pk'):
            self._data['user'] = value
            self.user_id = value.pk
        else:
            self._data = None
            self.user_id = None
    
    @user.deleter
    def user(self):
        self._data['user'] = None
        self.user_id = None


    def check_otp(self, otp):
        return check_password(otp, self.otp)

