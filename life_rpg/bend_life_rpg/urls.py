from bend_life_rpg import views
from django.urls import path


urlpatterns = [
    path('users/', views.snippet_list),
    path('register/', views.register),
]