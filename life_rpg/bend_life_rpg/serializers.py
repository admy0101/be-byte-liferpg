from rest_framework import serializers
from bend_life_rpg.models import Player, Item, Task
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

    
class UpdateCurrencySerializer(serializers.Serializer):
    add_currency = models.IntegerField(default=0)

    def validate(self, validated_data):
        user = self.request.user
        player =  Player.objects.get(id=user.id)
        data = validated_data
        print(data)
        buy_item = "buy_item" in data and data["buy_item"]
        add_currency = "add_currency" in data and data["add_currency"]
        change_xp = "change_xp" in data and Item.objects.get(item_name = data["change_xp"])



        # Change Currency
        # Change Experience
        # Buy Items
        if buy_item:
            if user.currency >= buy_item.price:
                user.currency -= buy_item.price
                user.inventory.add(buy_item)
                user.save()

        if add_currency:
            player.currency += add_currency
            player.save()

        return player
