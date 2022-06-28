from bend_life_rpg import views
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'players', views.UserViewSet)

router.register(r'shops', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', views.register),
]
