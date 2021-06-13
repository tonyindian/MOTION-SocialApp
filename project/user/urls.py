from django.urls import path

from project.user.views import ListUsersAPIView, ToggleFollowerAPIView, ListFollowersAPIVIew, ListFollowingAPIView

urlpatterns = [
    path('users/', ListUsersAPIView.as_view()),
    path('social/followers/toggle-follow/<int:id>/', ToggleFollowerAPIView.as_view()),
    path('social/followers/followers/', ListFollowersAPIVIew.as_view()),
    path('social/followers/following/', ListFollowingAPIView.as_view())
]
