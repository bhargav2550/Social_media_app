from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


