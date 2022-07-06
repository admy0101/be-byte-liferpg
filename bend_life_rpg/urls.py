from bend_life_rpg import views
from django.urls import path, include
from bend_life_rpg.views import LoginView, LogoutView, ProfileView, RegisterView, ShopView, ItemView, TaskView, RoomView, get_csrf

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'shops', views.ShopView)
# router.register(r'rooms', views.RoomView)

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('items/', ItemView.as_view()),
    path('tasks/', TaskView.as_view({"get": "list"})),
    path('tasks/add/', TaskView.as_view({"post": "create"})),
    path('tasks/edit/<int:pk>', TaskView.as_view({"patch": "partial_update"})),
    path('tasks/delete/<int:pk>', TaskView.as_view({"delete": "destroy"})),
    path("csrf/", get_csrf, name="csrf"),
    path('rooms/', RoomView.as_view({"get": "list"})),
    path('rooms/edit/<int:pk>', RoomView.as_view({"patch": "partial_update"}))

]
