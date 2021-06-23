from django.contrib import admin

# Register your models here.
from project.authprofile.models import AuthProfile

admin.site.register(AuthProfile)
