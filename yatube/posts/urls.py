# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:sl>/', views.group_posts),
] 