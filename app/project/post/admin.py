from django.contrib import admin

# Register your models here.
from app.project.post.models import Post

admin.site.register(Post)
