from django.db.models import Q
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import FriendRequest
from project.friendrequest.permissions import IsMentionedOrSuperuser, IsReceiverOrSuperuser
from project.friendrequest.serializers import FriendRequestSerializer
from ..helpers.email import send_email
from ..user.models import User
from project.user.serializers import PublicInfoUserSerializer


class CreateFriendRequestAPIView(CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     user_id = self.kwargs['id']
    #     new_friend = User.objects.get(id=user_id)
    #     serializer.save(requester=self.request.user, receiver=new_friend)
    #     subject = f'{requester.first_name} {requester.last_name} wants to be your friend!'
    #     message = f' Hi {new_friend.first_name} \n ' \
    #     f'You have a new friend request from {requester.first_name} {requester.last_name} '
    #     recipient = new_friend.data.get('email')
    #     send_email(subject, message, recipient)
    #
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        user_id = self.kwargs['id']
        new_friend = User.objects.get(id=user_id)
        requester = self.request.user
        receiver = new_friend
        serializer.save(requester=requester, receiver=receiver)
        subject = f'{requester.first_name} {requester.last_name} wants to be your friend!'
        message = f' Hi {new_friend.first_name} \n ' \
                  f'You have a new friend request from {requester.first_name} {requester.last_name} '
        recipient = new_friend.email
        send_email(subject, message, recipient)
        return Response(serializer.data)


class ListFriendsAPIView(GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = PublicInfoUserSerializer
    permission_classes = [IsMentionedOrSuperuser]

    def get(self, request, *args, **kwargs):
        list = []
        queryset = self.get_queryset().filter(Q(requester=request.user) |
                                              Q(receiver=request.user), status='accepted')
        for friendrequest in queryset:
            if friendrequest.receiver == request.user:
                list.append(friendrequest.requester)
            if friendrequest.requester == request.user:
                list.append(friendrequest.receiver)
        serializer = self.get_serializer(list, many=True)
        return Response(serializer.data)


class RetrieveUpdateDeleteFriendRequestAPIView(GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        self.permission_classes = [IsMentionedOrSuperuser]
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsReceiverOrSuperuser]
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsMentionedOrSuperuser]
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
