from bend_life_rpg import views
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)

router.register(r'shops', views.ShopItemViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', views.register),
    path('user/<int:id>/', views.user)
]
