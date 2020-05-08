# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User  # Django Build in User Model
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat_room.models import Room  # Our Room model
from chat_room.serializers import RoomSerializer, UserSerializer # Our Serializer Classes


# Users View
@csrf_exempt # Decorator to make the view csrf excempt.
def user_list(request, pk=None):
    #List all required users, or create a new user.
    if request.method == 'GET':
        if pk: # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id=pk) # Select only that particular user
        else:
            users = User.objects.all() # Else get all user list
        serializer = UserSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)   # Return serialized data
    elif request.method == 'POST':
        data = JSONParser().parse(request)     # On POST, parse the request object to obtain the data in json
        serializer = UserSerializer(data=data)   # Seraialize the data
        if serializer.is_valid():
            serializer.save()  # Save it if valid
            return JsonResponse(serializer.data, status=201)     # Return back the data on success
        return JsonResponse(serializer.errors, status=400)     # Return back the errors  if not valid

@csrf_exempt
def room_list(request, owner=None, member=None):
    # List all required room, or create a new room.
    if request.method == 'GET':
        # rooms = Room.objects.filter(owner_id=owner, member_id=member)
        rooms = Room.objects.all() #get all rooms lists
        serializer = RoomSerializer(rooms, many=True, context={'request': request})
        print('----------------')
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def join_room(request, room_id): # Join room based on the room id of the created room
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            room = Room.objects.filter(id=room_id)
        except Exception as e:
            return JsonResponse({'message': 'Room does not exist.',
                                 'details': str(e)})

        user = request.user
        room.members.add(user)
        room.save()
        serializer = RoomSerializer(room, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
