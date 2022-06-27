from django.shortcuts import render
import json
from types import SimpleNamespace
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.contrib.auth.models import User
from bend_life_rpg.serializers import UserSerializer


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



class single_user(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return User.objects.filter(username=username)
