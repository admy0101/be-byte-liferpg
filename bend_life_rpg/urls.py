from bend_life_rpg import views
from django.urls import path, include
from bend_life_rpg.views import LoginView, ProfileView, RegisterView, ShopView, ItemView, get_csrf

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'shops', views.ShopView)
router.register(r'tasks', views.TaskView)
router.register(r'rooms', views.RoomView)

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('items/', ItemView.as_view()),
    path("csrf/", get_csrf, name="csrf"),

]
