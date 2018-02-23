from rest_framework import serializers
from profiles.models import Profile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    email = serializers.EmailField(required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user