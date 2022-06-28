from django.db import models

class Shop (models.Model):
    shop = models.CharField

class ShopItem (models.Model):
    item_name = models.CharField
    price = models.IntegerField
    unlock_xp = models.IntegerField
    description = models.CharField
    category = models.CharField
    room_category = models.CharField
    sprite = models.CharField
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)