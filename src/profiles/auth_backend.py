from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.hashers import make_password, check_password
import re


class CustomModelBackend(ModelBackend):

  def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        profile = None
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            if '@' in username:
                UserModel.USERNAME_FIELD = 'email'
            elif self.is_valid_mobile_number(username):
                profile = Profile.objects.get(mobile_number=username)

            if profile:
                username = profile.user.username                

            user = UserModel._default_manager.get_by_natural_key(username)
            profile = Profile.objects.get(user_id=user.id)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)
        else:
            valid_password = user.check_password(password)
            if not valid_password and profile:
                valid_password = profile.check_otp(password)
            
            if valid_password and self.user_can_authenticate(user):
                return user

  def is_valid_mobile_number(self, username):
    Pattern = re.compile("[7-9][0-9]{9}")
    return Pattern.match(username)