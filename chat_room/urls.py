from django.urls import path
from . import views
from .views import RoomViewSet

join_room_view = RoomViewSet.as_view(actions={
    'put': 'join_room'
})

urlpatterns = [
    # URL form : "/api/rooms/1/2"
    path('api/rooms/<int:owner>/<int:member>', views.room_list, name='room-detail'),  # For GET request.
    # URL form : "/api/rooms/"
    path('api/rooms/', views.room_list, name='room-list'),   # For POST
    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
    path('<str:room_timestamp>', join_room_view)
]