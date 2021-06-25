from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, GenericAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters

from project.helpers.email import send_email
from project.post.permissions import IsAuthorOrSuperuserOrReadOnly
from project.user.serializers import UserSerializer, FollowersSerializer, FollowingSerializer,\
    PrivateInfoUserSerializer, PublicInfoUserSerializer

User = get_user_model()


class ListUsersAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PublicInfoUserSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ['first_name', 'last_name', 'username']

    # def get_queryset(self):
    #
    #     #search = self.request.GET.get('search')
    #     if search:
    #         #result = self.queryset.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(username__icontains=search))
    #     else:
    #         result = self.queryset.all()
    #     return result


class ToggleFollowerAPIView(GenericAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_id = self.kwargs['id']
        # the sender of the follow request
        follower = self.request.user
        # the recipient of the follow request
        followee = User.objects.get(id=user_id)

        if followee in follower.followees.all():
            follower.followees.remove(followee)
        else:
            follower.followees.add(followee)
        followee.save()

        subject = 'You have new follower'
        message = f' Hi {followee.first_name} \n ' \
                  f'{follower.first_name} {follower.last_name} is now following you! '
        recipient = followee.email
        send_email(subject, message, recipient)

        return Response(self.get_serializer(followee).data)


class ListFollowersAPIVIew(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FollowersSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj


class ListFollowingAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FollowingSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj


class RetrieveUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    permission_classes = [IsAuthorOrSuperuserOrReadOnly]


class RetrieveUpdateSelfAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PrivateInfoUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj
