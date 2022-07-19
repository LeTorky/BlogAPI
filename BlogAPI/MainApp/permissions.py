from rest_framework import permissions

class PostsPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("Test")
        if request.method in permissions.SAFE_METHODS:
            return True
        print("Test")
        return False