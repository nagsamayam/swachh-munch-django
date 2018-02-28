from rest_framework import serializers
from profiles.models import Profile
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator


User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    email = serializers.EmailField(required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=3, max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user