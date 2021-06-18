from rest_framework.permissions import BasePermission, SAFE_METHODS


# object level permission
class IsAuthorOrSuperuserOrReadOnly(BasePermission):
    """
    if GET => everyone can see it. if PUT/PATCH/DELETE => only author and superuser can do it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author or request.user.is_superuser
