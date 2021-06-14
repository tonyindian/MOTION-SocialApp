from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PublicInfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FollowersSerializer(serializers.ModelSerializer):
    followers = PublicInfoUserSerializer(many=True)

    class Meta:
        model = User
        fields = ['followers']


class FollowingSerializer(serializers.ModelSerializer):
    followees = PublicInfoUserSerializer(many=True)

    class Meta:
        model = User
        fields = ['followees']
