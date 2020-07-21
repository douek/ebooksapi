from rest_framework import permissions
import logging

class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        isAdmin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or isAdmin

class IsReviewAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            
            return True
        return obj.review_author == request.user