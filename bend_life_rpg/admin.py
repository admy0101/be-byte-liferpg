from django.contrib import admin
from django.contrib.auth.models import User

from bend_life_rpg.models import Shop, Item, Task, Player, Room

admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Task)
admin.site.register(Player)
admin.site.register(Room)
