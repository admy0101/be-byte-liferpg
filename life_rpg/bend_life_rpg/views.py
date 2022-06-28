from django.shortcuts import render
import json
from types import SimpleNamespace
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from bend_life_rpg.serializers import ShopItemSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from bend_life_rpg.models import ShopItem

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print(serializer, users)
        return JsonResponse(serializer.data, safe=False)


        
@csrf_exempt
def user(request, id):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(request, id)
        user = User.objects.get(pk=id)


        serializer = UserSerializer(user)
        serializer.data
        return JsonResponse(serializer.data, safe=False)



        
@csrf_exempt
def register(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        newUser = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
        user = User(username = newUser.username)
        user.save()

        serializer = UserSerializer(user)
        serializer.data
        print(serializer, user)
        return JsonResponse(serializer.data, safe=False)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    
    # def perform_create(self, serializer):
    #     print(serializer, self)
    #     serializer.set_password(serializer.data.password)
    #     serializer.save()

class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    permission_classes = []