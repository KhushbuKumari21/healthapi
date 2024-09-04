# core/permissions.py
from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

class IsPatient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
