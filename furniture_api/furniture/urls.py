from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FurnitureViewSet, UserViewSet, OrderViewSet, InventoryViewSet,
    ReviewViewSet, CustomizationViewSet, WishlistViewSet, PromotionViewSet,
    OrderPromotionViewSet, AssemblyGuideViewSet, home
)

# Create the router for URL routing
router = DefaultRouter()

# Register all viewsets with the router
router.register(r'furniture', FurnitureViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'customizations', CustomizationViewSet)
router.register(r'wishlist', WishlistViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'order-promotions', OrderPromotionViewSet)
router.register(r'assembly-guides', AssemblyGuideViewSet)

# URL patterns for the API
urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('', include(router.urls)),  # All API endpoints at root
]