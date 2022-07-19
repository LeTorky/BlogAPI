from rest_framework import permissions
import jwt
import environ
from django.contrib.auth import authenticate


env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')

class PostsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        user = jwt.decode(request.headers['Authorization'].split(' ')[1], SECRET_KEY, algorithms=['HS256'])
        if authenticate(username = user['username'], password = user['password']):
            if obj.author.user.id == user['id']:
                return True
        return False

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action == 'login':
            return True
        user = jwt.decode(request.headers['Authorization'].split(' ')[1], SECRET_KEY, algorithms=['HS256'])
        if authenticate(username = user['username'], password = user['password']):
            if obj.id == user['id']:
                return True
        return False