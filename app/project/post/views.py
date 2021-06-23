from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, \
    RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .permissions import IsAuthorOrSuperuserOrReadOnly
from .serializers import PostSerializer, LikesOfUserSerializer, CreatePostSerializer
from ..friendrequest.models import FriendRequest

User = get_user_model()


class ListCreatePostsView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['text_content']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreatePostSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDeletePostsView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    permission_classes = [IsAuthorOrSuperuserOrReadOnly]


class ToggleLikePostAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['id']
        post_to_like = Post.objects.get(id=post_id)
        if self.request.user in post_to_like.likes.all():
            post_to_like.likes.remove(self.request.user)
        else:
            post_to_like.likes.add(self.request.user)
        post_to_like.save()
        return Response(self.get_serializer(post_to_like).data)


class ListLikesOfUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LikesOfUserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj


class ListFollowingPostsAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # URL params filtering
    def get(self, request, *args, **kwargs):
        followees = self.request.user.followees.all()
        queryset = self.get_queryset().filter(author__in=followees)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListUsersPostAPIView(GenericAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer

    # URL params filtering
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        queryset = self.get_queryset().filter(author=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListFriendsPostsAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        friendrequests = FriendRequest.objects.all().filter(Q(requester=request.user) |
                                                            Q(receiver=request.user), status='accepted')
        friends = []
        for friendrequest in friendrequests:
            if friendrequest.receiver == request.user:
                friends.append(friendrequest.requester)
            if friendrequest.requester == request.user:
                friends.append(friendrequest.receiver)

        queryset = self.get_queryset().filter(author__in=friends)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
