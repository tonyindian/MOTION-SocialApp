from rest_framework import status
from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Comment

from .serializer import CommentSerializer
# from ..post.models import Post


class ListCreateComment(ListCreateAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        author = self.request.user
        post = self.kwargs['id']
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author, post_id=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = Comment.objects.filter(post_id=self.kwargs['id'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

#
# class PostCommentAPIView(GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = 'id'
#
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def post(self, request):
#         post = self.get_object()
#         serializer = self.get_serializer(data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(author=self.request.user, post=post)
#         return Response(serializer.data)
#
