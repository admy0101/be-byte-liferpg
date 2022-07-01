from life_rpg.bend_life_rpg import views
from django.urls import path, include
from life_rpg.bend_life_rpg.views import LoginView, ProfileView

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'players', views.UserViewSet)

router.register(r'shops', views.ItemViewSet)

router.register(r'life_rpg.tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', views.register),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view())
]
