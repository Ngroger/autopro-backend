from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Room, Message
from .serializers import UserSerializer, RoomSerializer, MessageSerializer

class UserModelView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoomModelView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageModelView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer