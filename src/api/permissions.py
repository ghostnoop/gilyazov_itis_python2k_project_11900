from rest_framework import permissions

from core.models import Point


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.client.user_id == request.user.id
