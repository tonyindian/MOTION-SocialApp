import datetime
import math
from random import random

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from project.authprofile.models import AuthProfile
from project.authprofile.serializers import AuthProfileSerializer
from project.helpers.email import send_email
from project.user.serializers import PrivateInfoUserSerializer

User = get_user_model()


class RegisterNewUserAPIView(CreateAPIView):
    queryset = AuthProfile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AuthProfileSerializer

    def perform_create(self, serializer):
        user = User.objects.create_user(self.request.data.get('email').split('@')[0], self.request.data.get('email'))
        verification_code = math.floor(random() * 1000000)
        subject = 'Your verification code'
        message = 'Enter this code to verify your account: ' + verification_code
        recipient = self.request.data.get('email')
        send_email(subject, message, recipient)
        serializer.save(user=user, verification_code=verification_code)
        return Response(status=HTTP_200_OK)


class ValidateNewUserAPIView(GenericAPIView):
    queryset = AuthProfile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AuthProfileSerializer

    def post(self, request, *args, **kwargs):
        verification_code = int(request.data.get('verification_code'))
        user = User.objects.get(email=request.data.get('email'))
        extracted_keys = ["email", "username", "first_name", "last_name"]
        new_user_values = {key: request.data[key] for key in extracted_keys}
        new_user_values["password"] = make_password(self.request.data.get('password'))

        if verification_code == user.auth_profile.verification_code:
            user_serializer = PrivateInfoUserSerializer(user, data=new_user_values, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            verified_status = {"verified": "True"}
            auth_profile_serializer = self.get_serializer(user.auth_profile, data=verified_status, partial=True)
            auth_profile_serializer.is_valid(raise_exception=True)
            auth_profile_serializer.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(GenericAPIView):
    queryset = AuthProfile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AuthProfileSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(email=request.data.get('email'))
        verification_code = math.floor(random() * 1000000)
        new_code = {"verification_code": verification_code, "last_generated": datetime.datetime}
        auth_profile_serializer = self.get_serializer(user.auth_profile, data=new_code, partial=True)
        auth_profile_serializer.is_valid(raise_exception=True)
        auth_profile_serializer.save()
        subject = 'Reset password'
        message = 'Enter this verification code in the form to change your password: ' + str(verification_code)
        recipient = request.data.get('email')
        send_email(subject, message, recipient)
        return Response(status=HTTP_200_OK)


class ValidateNewPasswordAPIView(GenericAPIView):
    queryset = AuthProfile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AuthProfileSerializer

    def post(self, request, *args, **kwargs):
        verification_code = int(request.data.get('verification_code'))
        user = User.objects.get(email=request.data.get('email'))
        new_user_values = {"password": make_password(self.request.data.get('password'))}

        if verification_code == user.auth_profile.verification_code:
            user_serializer = PrivateInfoUserSerializer(user, data=new_user_values, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
