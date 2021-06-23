from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AuthProfile(models.Model):
    verification_code = models.IntegerField()
    last_generated = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)
    user = models.OneToOneField(to=User, null=False, blank=False,
                                on_delete=models.CASCADE, related_name='auth_profile')
