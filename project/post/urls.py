from django.urls import path

from project.post.views import ListCreatePostsView

urlpatterns = [
    path('',ListCreatePostsView.as_view()),
]