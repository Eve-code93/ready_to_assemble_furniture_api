from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, FurnitureViewSet, OrderViewSet, InventoryViewSet, 
    ReviewViewSet, CustomizationViewSet, WishlistViewSet, 
    PromotionViewSet, OrderPromotionViewSet, AssemblyGuideViewSet
)
from django.http import JsonResponse

# Create a router for automatic URL routing
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'furniture', FurnitureViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'customizations', CustomizationViewSet)
router.register(r'wishlist', WishlistViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'order-promotions', OrderPromotionViewSet)
router.register(r'assembly-guides', AssemblyGuideViewSet)

# Define the home view
def home(request):
    return JsonResponse({"message": "Welcome to the Furniture API! Use /api/ to access the API."})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Homepage
    path('api/', include(router.urls)),  # Include all API endpoints under /api/
    path('auth/', include('dj_rest_auth.urls')),  # Authentication URLs
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration URLs
    path('accounts/', include('allauth.urls')),  # For email verification
]
