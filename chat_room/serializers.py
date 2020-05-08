# serializers from rest_framework to make use of the serializer classes.

from django.contrib.auth.models import User
from rest_framework import serializers
from chat_room.models import Room

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    #The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with
    # fields that correspond to the Model fields.
    password = serializers.CharField(write_only=True)
    #password is specified write_only to avoid getting the password displayed on GET request
    class Meta:
        model = User
        fields = ['username', 'password']

# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    #serialized as SlugRelatedField to represent the target of the relationship using a field on the target.
    # The field is specified as slug_field.
    # It also takes a 'many' argument which identifies the relation is many-to-many or not.
    # We gave it false, since a room can only contain a single owner.
    # The 'queryset' argument takes the list of objects from which the related object is to be chosen.
    member = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Room
        fields = ['owner', 'member', 'name', 'timestamp']