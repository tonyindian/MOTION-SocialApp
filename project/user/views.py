from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404, GenericAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.post.permissions import IsAuthorOrSuperuserOrReadOnly
from project.user.serializers import UserSerializer, FollowersSerializer, FollowingSerializer

User = get_user_model()


class ListUsersAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


# class ToggleFollowerAPIView(UpdateAPIView):
#     queryset = User.objects.all()
#     lookup_field = 'id'
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer
#
#     def perform_update(self, serializer):
#         if serializer.instance in self.request.user.followees.all():
#             self.request.user.followees.remove(serializer.instance)
#         else:
#             self.request.user.followees.add(serializer.instance)
#         serializer.save()

class ToggleFollowerAPIView(GenericAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_id = self.kwargs['id']
        user_to_follow = User.objects.get(id=user_id)
        if user_to_follow in self.request.user.followees.all():
            self.request.user.followees.remove(user_to_follow)
        else:
            self.request.user.followees.add(user_to_follow)
        user_to_follow.save()
        return Response(self.get_serializer(user_to_follow).data)


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
