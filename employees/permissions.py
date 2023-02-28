from .models import User
from rest_framework import permissions
from rest_framework.views import View, Request


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user
