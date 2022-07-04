from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
User._meta.get_field('email').blank = False

class Shop (models.Model):
    display_name = models.CharField(max_length=100, default="Furniture Shop")

    def __str__(self):
        return self.display_name

class Item (models.Model):
    item_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, blank=False)
    unlock_xp = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
    sprite = models.ImageField(upload_to='static')
    bought = models.BooleanField()

    def __str__(self):
        return self.item_name

class Player(User):
    experience = models.IntegerField(default=0)
    currency = models.PositiveIntegerField(default=0)
    avatar = models.URLField(default="https://miro.medium.com/max/720/1*W35QUSvGpcLuxPo3SRTH4w.png")
    inventory = models.ManyToManyField(to=Item,  blank=True)

class Task (models.Model):
    task_name = models.CharField(max_length=250)
    task_difficulty = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    is_complete = models.BooleanField(default=False)
    task_owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    def __str__(self):
        return self.task_name


class Room (models.Model):
    room_owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    shop_items = models.ManyToManyField(to=Item, blank=True)
    
    room_type = models.CharField(max_length=50)
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name
