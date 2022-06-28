from django.shortcuts import render
import json
from types import SimpleNamespace
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bend_life_rpg.models import Player
from bend_life_rpg.serializers import ItemSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from bend_life_rpg.models import Item

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = UserSerializer(players, many=True)
        print(serializer, players)
        return JsonResponse(serializer.data, safe=False)


        
@csrf_exempt
def user(request, id):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(request, id)
        player = Player.objects.get(pk=id)


        serializer = UserSerializer(player)
        serializer.data
        return JsonResponse(serializer.data, safe=False)



        
@csrf_exempt
def register(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        newUser = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
        user = Player(username = newUser.username)
        user.save()

        serializer = UserSerializer(user)
        serializer.data
        print(serializer, user)
        return JsonResponse(serializer.data, safe=False)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    
    # def perform_create(self, serializer):
    #     print(serializer, self)
    #     serializer.set_password(serializer.data.password)
    #     serializer.save()

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = []