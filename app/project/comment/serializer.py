from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Comments
from .. import settings

User = settings.AUTH_USER_MODEL


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'
