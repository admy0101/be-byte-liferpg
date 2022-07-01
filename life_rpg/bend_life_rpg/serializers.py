from rest_framework import serializers
from life_rpg.bend_life_rpg.models import Player, Item, Task
from django.contrib.auth import authenticate
from django.db import models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ['id', 'username', 'email', 'currency', 'experience', 'password', 'avatar']

    def create(self, data):
        password = data.pop('password', None)
        instance = super().create(data)
        instance.set_password(password)
        instance.save()
        return instance

# def create(self, validated_data):
#     return User.objects.create(**validated_data)


# def update(self, instance, validated_data):
#     instance.username = validated_data.get('username', instance.username)
#     instance.save()
#     return instance

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'unlock_xp', 'description', 'category', 'sprite', 'shop']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task', 'task_difficulty', 'is_complete']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username", write_only=True)

    password = serializers.CharField(label="Password", style={'input_type': 'password'}, trim_whitespace=False, write_only=True)

    def validate(self, attributes):
        username = attributes.get('username')
        password = attributes.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Wrong Username or Password'
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Both "Username" and "Password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

        
        attributes['user'] = user
        return attributes

    
class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['username', 'email', 'currency', 'experience', 'avatar']
