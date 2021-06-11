from django.urls import path

from project.user.views import ListUsersAPIView

urlpatterns = [
    path('', ListUsersAPIView.as_view())
]
