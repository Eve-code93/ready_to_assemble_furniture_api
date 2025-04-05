from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import (
    User, Furniture, Order, Inventory, Review, 
    Customization, Wishlist, Promotion, OrderPromotion, AssemblyGuide
)
from .serializers import (
    UserSerializer, FurnitureSerializer, OrderSerializer, InventorySerializer, 
    ReviewSerializer, CustomizationSerializer, WishlistSerializer, 
    PromotionSerializer, OrderPromotionSerializer, AssemblyGuideSerializer
)
from .permissions import AdminOnly 

# General views
def home(request):
    return JsonResponse({"message": "Welcome to the Furniture API!"})

def render_home(request):
    return render(request, 'home.html')

# User ViewSet
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Open to all users for registration

# Furniture ViewSet
class FurnitureViewSet(ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']

# Order ViewSet
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Restricted to authenticated users

# Inventory ViewSet
class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [AdminOnly]  # Only accessible by admins

# Review ViewSet
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users can add reviews

# Customization ViewSet
class CustomizationViewSet(ModelViewSet):
    queryset = Customization.objects.all()
    serializer_class = CustomizationSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

# Wishlist ViewSet
class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

# Promotion ViewSet
class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [AdminOnly]  # Accessible by admins only

# Order Promotion ViewSet
class OrderPromotionViewSet(ModelViewSet):
    queryset = OrderPromotion.objects.all()
    serializer_class = OrderPromotionSerializer
    permission_classes = [AdminOnly]  # Restricted to admins

# Assembly Guide ViewSet
class AssemblyGuideViewSet(ModelViewSet):
    queryset = AssemblyGuide.objects.all()
    serializer_class = AssemblyGuideSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users can access guides
