from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='carla-dash'),
    path('canbus', views.canbus, name='carla-dash'),
]
