from django.contrib.auth.models import AbstractUser
from django.db import models

from project import settings


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    followees = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='followers')

    def __str__(self):
        return self.username
