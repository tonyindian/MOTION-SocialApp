from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'{instance.id}/{filename}'


class Post(models.Model):

    text_content = models.TextField()
    images = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name='posts')
    likes = models.ManyToManyField(User, blank=True, related_name='posts_liked')

    def __str__(self):
        return f"Post: {self.id}, Author: {self.author}"

    class Meta:
        ordering = ['-created']
