from rest_framework import serializers
from basic.models import Channel, Comment
from rest_framework_mongoengine.serializers import DocumentSerializer


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('title', 'type', 'platform', 'archived')

class TestSerializer(DocumentSerializer):
    class Meta:
        model = Comment
        fields = '__all__'