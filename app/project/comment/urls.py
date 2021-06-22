from django.urls import path

from project.comment.views import PostCommentAPIView

urlpatterns = [
    path('<int:id>/', PostCommentAPIView.as_view()),
]
