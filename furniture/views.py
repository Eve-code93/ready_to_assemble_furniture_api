from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import (
    User, Furniture, Order, Inventory, Review, 
    Customization, Wishlist, Promotion, OrderPromotion, AssemblyGuide
)
from .serializers import (
    UserSerializer, FurnitureSerializer, OrderSerializer, InventorySerializer, 
    ReviewSerializer, CustomizationSerializer, WishlistSerializer, 
    PromotionSerializer, OrderPromotionSerializer, AssemblyGuideSerializer
)
from django.http import JsonResponse
from django.shortcuts import render
#filtering and search
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .models import Furniture
from .serializers import FurnitureSerializer


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Anyone can register

# Furniture ViewSet
class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]  # Open to all users

# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can order

# Inventory ViewSet
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]  # Only admins should ideally manage stock

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # Users must be logged in to review

# Customization ViewSet
class CustomizationViewSet(viewsets.ModelViewSet):
    queryset = Customization.objects.all()
    serializer_class = CustomizationSerializer
    permission_classes = [IsAuthenticated]

# Wishlist ViewSet
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

# Promotion ViewSet
class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticated]  # Admins should manage promotions

# Order Promotion ViewSet
class OrderPromotionViewSet(viewsets.ModelViewSet):
    queryset = OrderPromotion.objects.all()
    serializer_class = OrderPromotionSerializer
    permission_classes = [IsAuthenticated]

# Assembly Guide ViewSet
class AssemblyGuideViewSet(viewsets.ModelViewSet):
    queryset = AssemblyGuide.objects.all()
    serializer_class = AssemblyGuideSerializer
    permission_classes = [IsAuthenticated]  # Admins should upload guides



from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Furniture API!"})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


#filtering and search
class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Define filter fields
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']