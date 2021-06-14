from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post
User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikesOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['posts_liked']
