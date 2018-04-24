from rest_framework import permissions
from accounts.models import UserProfile
from flashcards.models import Deck

class IsDeckOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.parent_user == request.user

class IsCardOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.parent_deck.parent_user == request.user) or (request.user.is_superuser)
