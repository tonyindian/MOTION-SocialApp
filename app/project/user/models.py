from django.contrib.auth.models import AbstractUser
from django.db import models

from project import settings


def user_directory_path(instance, filename):
    return f'{instance.username}/{filename}'


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    followees = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='followers')

    def __str__(self):
        return self.username
