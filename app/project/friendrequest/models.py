from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class FriendRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.TextField(default='pending')
    requester = models.ForeignKey(to=User, related_name='requested', on_delete=models.CASCADE)
    receiver = models.ForeignKey(to=User, related_name='received', on_delete=models.CASCADE)
