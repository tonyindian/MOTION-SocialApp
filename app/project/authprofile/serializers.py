from rest_framework import serializers

from project.authprofile.models import AuthProfile


class AuthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthProfile
        fields = '__all__'
        read_only_fields = ['verification_code', 'user']
