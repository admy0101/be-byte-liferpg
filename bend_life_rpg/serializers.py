from rest_framework import serializers
from bend_life_rpg.models import Player, Item, Room, Shop, Task
from django.contrib.auth import authenticate
from django.db import models


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username", write_only=True)
    email = serializers.EmailField(label="E-Mail", write_only=True)
    password = serializers.CharField(label="Password", style={
                                     'input_type': 'password'}, trim_whitespace=False, write_only=True)

    def validate(self, attributes):
        username = attributes.get('username')
        password = attributes.get('password')

        if username and password:
           return attributes

        else:
            msg = 'Both "Username" and "Password" are required.'
            raise serializers.ValidationError(msg, code='authorization')



class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'display_name']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'unlock_xp',
                  'description', 'sprite', 'shop']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_difficulty', 'is_complete']

    def create(self, validated_data):
        user = self.context['request'].user
        player =  Player.objects.get(id=user.id)
        return Task.objects.create(
        task_name=validated_data['task_name'],
        task_difficulty=validated_data['task_difficulty'],
        task_owner=player
    )

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['room_name', 'room_type', 'shop_items']

    def create(self, validated_data):
        user = self.context['request'].user
        player =  Player.objects.get(id=user.id)
        return Room.objects.create(
        room_name=validated_data['room_name'],
        room_type=validated_data['room_type'],
        # shop_items=validated_data['shop_items'],
        room_owner=player
    )    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username", write_only=True)

    password = serializers.CharField(label="Password", style={
                                     'input_type': 'password'}, trim_whitespace=False, write_only=True)

    def validate(self, attributes):
        username = attributes.get('username')
        password = attributes.get('password')

        if username and password:
            user = authenticate(request=self.context.get(
                'request'), username=username, password=password)

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
        fields = ['username', 'email', 'currency', 'experience', 'avatar', 'inventory']
