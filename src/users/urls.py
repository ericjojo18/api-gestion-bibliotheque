from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets.user_viewsets import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]