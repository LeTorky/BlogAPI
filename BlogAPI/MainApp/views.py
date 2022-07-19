from email import header
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth import authenticate
from .permissions import *
import jwt
import environ

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=False, methods=['get'], url_path=r'byAuthor/(?P<pk>[0-9]+)', permission_classes=[AllowAny])
    def get_blogs_by_author(self, request, pk):
        author = Author.objects.get(pk=pk)
        posts = Post.objects.filter(author=author)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=[AllowAny])
    def login(self, request):
        user = self.serializer_class(data=request.data)
        user.is_valid()
        username = user.data['username']
        password = user.data['password']
        id = User.objects.get(username=username).id
        if authenticate(username = username, password = password):
            encoded_jwt = jwt.encode({"id": id, "username":username, "password":password}, SECRET_KEY, algorithm="HS256")
            return Response({"success": True}, headers={'Authorization': 'Bearer ' + encoded_jwt})
        else:
            return Response({"success": False})
