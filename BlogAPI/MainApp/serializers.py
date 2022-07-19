from sqlite3 import IntegrityError
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

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    class Meta:
        model = UserAuthorDTO
        fields = ('username', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        name = validated_data.pop('name')
        user = UserAuthorDTO(**validated_data)
        user.set_password(validated_data['password'])
        user.name = name
        return user
