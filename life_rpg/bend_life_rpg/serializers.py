from rest_framework import serializers
from bend_life_rpg.models import Player, Item, Task
from django.db import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = models.EmailField(("email address"))

    class Meta:
        model = Player
        fields = ['id', 'username', 'email', 'experience', 'password']

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
