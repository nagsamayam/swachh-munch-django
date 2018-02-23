from rest_framework import serializers
from basic.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('title', 'type', 'platform', 'archived')