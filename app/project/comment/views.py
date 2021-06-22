from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Comments
from .serializer import CommentSerializer
from ..post.models import Post


class PostCommentAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment = self.get_serializer(request.data)
        post.post_comments.add(comment)
        post.save()
        return Response(self.get_serializer(comment).data)
