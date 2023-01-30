from rest_framework import permissions


class IsRead(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ("PUT", "PATCH")


class IsWrite(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.method in permissions.SAFE_METHODS
