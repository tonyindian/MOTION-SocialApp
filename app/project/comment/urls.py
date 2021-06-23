from django.urls import path

from project.comment.views import ListCreateComment

urlpatterns = [
    path('<int:id>/', ListCreateComment.as_view()),
]
