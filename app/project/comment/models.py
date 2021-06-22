from django.contrib.auth import get_user_model
from django.db import models

from project.post.models import Post

User = get_user_model()


class Comments(models.Model):
    text_content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_comments')

#
# class Meta:
#     ordering = ['-created']
