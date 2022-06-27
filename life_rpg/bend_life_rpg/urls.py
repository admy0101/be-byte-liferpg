from bend_life_rpg.views import user_list, register
from bend_life_rpg.views import single_user
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('users/', user_list),
    path('register/', register),
    re_path(r'^users/(?P<username>.+)/$', single_user.as_view())
]