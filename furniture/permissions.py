from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Allows access only to admin users."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()

class IsSeller(BasePermission):
    """Allows access only to sellers."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_seller()

class IsCustomer(BasePermission):
    """Allows access only to customers."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_customer()
