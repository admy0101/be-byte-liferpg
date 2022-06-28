from rest_framework import serializers
from django.contrib.auth.models import User
from bend_life_rpg.models import ShopItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

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

class ShopItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopItem
        fields = ['id', 'item_name', 'price', 'unlock_xp', 'description', 'category', 'room_category', 'sprite', 'shop']
        