from rest_framework import serializers
from bend_life_rpg.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=30)


def create(self, validated_data):
    return User.objects.create(**validated_data)


def update(self, instance, validated_data):
    instance.username = validated_data.get('username', instance.username)
    instance.save()
    return instance