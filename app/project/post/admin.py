from django.contrib import admin

# Register your models here.
from project.post.models import Post

admin.site.register(Post)
