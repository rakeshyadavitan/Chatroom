from django.conf.urls import url
from . import views

urlpatterns = [
    # URL form : "/api/rooms/1/2"
    # url('api/rooms/<int:owner>/<int:member>', views.room_list, name='room-detail'),  # For GET request.
    url('rooms', views.room_list, name='room-detail'),  # For GET all rooms request.
    # URL form : "/api/rooms/"
    # url('rooms/', views.room_list, name='room-list'),   # For POST
    # URL form "/api/users/1"
    # url('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    url('users', views.user_list, name='user-detail'),

    # url('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
    url('rooms/<int:room_timestamp>', views.join_room, name='join_room') # PUT for new member to join a room
]
