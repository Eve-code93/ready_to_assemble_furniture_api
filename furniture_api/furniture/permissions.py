from rest_framework.permissions import BasePermission

class AllowAllAuthenticated(BasePermission):
   
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    from rest_framework.permissions import BasePermission

class AdminOnly(BasePermission):
    """Allows access only to admin users."""
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a superuser (admin)
        return request.user.is_authenticated and request.user.is_superuser

class IsStaff(BasePermission):
    
    def has_permission(self, request, view):
        
        return request.user.is_authenticated and request.user.is_staff
class IsCustomer(BasePermission):
    
    def has_permission(self, request, view):
        
        return request.user.is_authenticated and getattr(request.user, 'is_customer', False)
