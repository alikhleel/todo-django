from rest_framework.permissions import BasePermission


class CanEditPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            workbook = view.get_object()
            if user.workbook_permissions.filter(workbook=workbook, can_edit=True).exists():
                return True
        return False


class CanViewPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            workbook = view.get_object()
            if user.workbook_permissions.filter(workbook=workbook).exists():
                return True
        return False
