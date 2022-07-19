from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    creation_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
