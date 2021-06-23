"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TEAMONE - MOTION Project",
      default_version='v1',
      description="Motion Social Network by Propulsion Academy students",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="teamonemotion@existiert.net"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,  # Set to False restrict access to protected endpoints
   permission_classes=(permissions.AllowAny,),  # Permissions for docs access
)

jwt_views = [
    path('', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api/social/posts/', include('project.post.urls')),
    path('backend/api/social/comments/', include('project.comment.urls')),
    path('backend/api/social/friends/', include('project.friendrequest.urls')),
    path('backend/api/', include('project.user.urls')),
    path('backend/api/auth/token/', include(jwt_views)),
    path('backend/api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('backend/api/auth/', include('project.authprofile.urls'))
]
