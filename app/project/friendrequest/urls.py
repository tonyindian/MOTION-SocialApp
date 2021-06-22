from django.urls import path
from project.friendrequest.views import CreateFriendRequestAPIView, RetrieveUpdateDeleteFriendRequestAPIView, \
    ListFriendsAPIView

urlpatterns = [
    path('', ListFriendsAPIView.as_view()),
    path('request/<int:id>/', CreateFriendRequestAPIView.as_view()),
    path('requests/<int:id>/', RetrieveUpdateDeleteFriendRequestAPIView.as_view())
]
