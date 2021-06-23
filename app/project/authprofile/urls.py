from django.urls import path

from project.authprofile.views import RegisterNewUserAPIView, ValidateNewUserAPIView, ResetPasswordAPIView, \
    ValidateNewPasswordAPIView

urlpatterns = [
    path('registration/', RegisterNewUserAPIView.as_view()),
    path('registration/validation/', ValidateNewUserAPIView.as_view()),
    path('password-reset/', ResetPasswordAPIView.as_view()),
    path('password-reset/validation/', ValidateNewPasswordAPIView.as_view())
]
