from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users edit content.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to staff users
        return request.user.is_staff


class IsSameUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow logged users see and edit his own content.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only if the logged user is the same as the object.
        return obj.username == request.user.username


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow Authors of an article to edit.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the article.
        return obj.author == request.user


class IsAuthorOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow Authors of an article and admins to edit.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions allowed to staff members
        if request.user.is_staff:
            return True

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the article.
        return obj.author == request.user


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit.
    Admin users however have access to all.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions allowed to staff members
        if request.user.is_staff:
            return True

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permissions are only to the owner of the profile
        return obj.username == request.user.username


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit.
    Admin users however have access to all.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions allowed to staff members
        if request.user.is_staff:
            return True

        # Permissions are only to the owner of the profile
        return obj.username == request.user.username
