from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset= Author.objects.all())
    class Meta:
        model = Author
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'