from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse

from .views import (
    UserViewSet, FurnitureViewSet, OrderViewSet, InventoryViewSet, 
    ReviewViewSet, CustomizationViewSet, WishlistViewSet, 
    PromotionViewSet, OrderPromotionViewSet, AssemblyGuideViewSet
)

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

# Swagger schema setup
schema_view = get_schema_view(
    openapi.Info(
        title="Furniture API",
        default_version="v1",
        description="API documentation for Ready-to-Assemble Furniture",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),

    # Swagger docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
