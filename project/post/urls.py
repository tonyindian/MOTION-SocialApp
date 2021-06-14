from django.urls import path

from project.post.views import ListCreatePostsView, RetrieveUpdateDeletePostsView, ToggleLikePostAPIView,\
    ListLikesOfUserAPIView, ListFollowingPostsAPIView, ListUsersPostAPIView

urlpatterns = [
    path('', ListCreatePostsView.as_view()),
    path('<int:id>/', RetrieveUpdateDeletePostsView.as_view()),
    path('toggle-like/<int:id>/', ToggleLikePostAPIView.as_view()),
    path('likes/', ListLikesOfUserAPIView.as_view()),
    path('following/', ListFollowingPostsAPIView.as_view()),
    path('user/<int:id>/', ListUsersPostAPIView.as_view())
]