from django.db import models
from django.contrib.auth.models import User

class Shop (models.Model):
    shop = models.CharField(max_length=100, default="Shop")
    category = models.CharField(max_length=50, default="Shop")

class Item (models.Model):
    item_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    unlock_xp = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="Shop")
    sprite = models.ImageField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

class Furniture(Item):
    room_category = models.CharField(max_length=100)

class Player(User):
    experience = models.IntegerField(default=0)
    avatar = models.URLField(default="https://miro.medium.com/max/720/1*W35QUSvGpcLuxPo3SRTH4w.png")
    currency = models.PositiveIntegerField(default=0)
    
class Inventory:
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
