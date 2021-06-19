from django.contrib import admin

# Register your models here.
from app.project.friendrequest.models import FriendRequest

admin.site.register(FriendRequest)
