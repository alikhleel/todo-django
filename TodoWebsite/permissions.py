from rest_framework import permissions


class IsAuthenticatedAndVerified(permissions.BasePermission):
    """
    Custom permission to only allow authenticated and verified users to access the API.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_email_confirmed
