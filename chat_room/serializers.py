from django.contrib.auth.models import User
from rest_framework import serializers
from chat_room.models import Room

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    """For Serializing Room"""
    owner = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    member = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = ['owner', 'member', 'name', 'timestamp']