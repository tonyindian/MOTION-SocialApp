from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


from .serializer import CommentSerializer
from ..post.models import Post


class PostCommentAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        post = self.get_object()
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user, post=post)
        return Response(serializer.data)
