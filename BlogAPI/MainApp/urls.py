from django.urls import path, include
from .views import *
from rest_framework import routers

default_router = routers.DefaultRouter()
default_router.register(r'authors', AuthorViewSet, basename='authors')
default_router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(default_router.urls)),
]