from rest_framework import serializers
from social_media_app.models import Post,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
