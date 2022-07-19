from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['get'], url_path=r'byAuthor/(?P<pk>[0-9]+)')
    def get_blogs_by_author(self, request, pk):
        author = Author.objects.get(pk=pk)
        posts = Post.objects.filter(author=author)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    