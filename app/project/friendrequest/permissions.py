from rest_framework.permissions import BasePermission, SAFE_METHODS


# object level permission
class IsMentionedOrSuperuser(BasePermission):
    """
    if GET => everyone can see it. if PUT/PATCH/DELETE => only author and superuser can do it
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.receiver or request.user == obj.requester or request.user.is_superuser


class IsReceiverOrSuperuser(BasePermission):
    """
    if GET => everyone can see it. if PUT/PATCH/DELETE => only author and superuser can do it
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.receiver or request.user.is_superuser
