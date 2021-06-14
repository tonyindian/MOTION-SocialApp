from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post
User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']


class LikesOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['posts_liked']

