import json
from types import SimpleNamespace

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status, views, viewsets, generics, filters
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth import login
from django.middleware.csrf import get_token
from bend_life_rpg.models import Item, Player, Shop, Task, Room
from bend_life_rpg.serializers import (CreateUserSerializer, ItemSerializer, LoginSerializer, ShopSerializer, TaskSerializer, RoomSerializer, CurrentUserSerializer)

def get_csrf(request):
    response = JsonResponse({"detail": get_token(request)})
    return response

class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=self.request.data, context={ 'request': self.request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = Player(username = data["username"], email = data["email"])
        user.set_password(data["password"])
        user.save()

        return Response(None, status=status.HTTP_202_ACCEPTED)

class ShopView(viewsets.ReadOnlyModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]

class ItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['shop', 'item', 'price']

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CurrentUserSerializer
    queryset = Player.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        player =  Player.objects.get(id=user.id)
        return player

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(task_owner=user.id)
        return tasks

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        rooms = Room.objects.filter(room_owner=user.id)
        if len(rooms) == 0:
            raise ValueError('A very specific bad thing happened. There are no rooms.')
        return rooms

