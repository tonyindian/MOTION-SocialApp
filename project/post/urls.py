from django.urls import path

from project.post.views import ListCreatePostsView, RetrieveUpdateDeletePostsView

urlpatterns = [
    path('', ListCreatePostsView.as_view()),
    path('<int:id>/', RetrieveUpdateDeletePostsView.as_view()),
]