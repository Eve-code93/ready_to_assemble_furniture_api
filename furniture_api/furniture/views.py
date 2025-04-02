from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import (
    User, Furniture, Order, Inventory, Review, 
    Customization, Wishlist, Promotion, OrderPromotion, AssemblyGuide
)
from .serializers import (
    UserSerializer, FurnitureSerializer, OrderSerializer, InventorySerializer, 
    ReviewSerializer, CustomizationSerializer, WishlistSerializer, 
    PromotionSerializer, OrderPromotionSerializer, AssemblyGuideSerializer
)
from .permissions import IsAdmin, IsSeller

# Pagination Class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Adjust page size as per requirement
    page_size_query_param = 'page_size'  # Allow users to set page size
    max_page_size = 100  # Limit max page size

# User ViewSet (Public Access)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Anyone can register

# Furniture ViewSet with Filtering, Searching, and Pagination
class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]  # Open to all users (adjust as needed)
    pagination_class = StandardResultsSetPagination  # Apply pagination

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'price']  # Enable filtering by category and price
    search_fields = ['name', 'description']  # Enable search by name and description
    ordering_fields = ['price', 'name']  # Enable ordering by price and name
    ordering = ['price']  # Default ordering (if no query param is passed)

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:  # Restrict these actions to authenticated users
            return [IsAuthenticated(), IsSeller()]
        return [AllowAny()]  # Allow any user to view furniture

# Order ViewSet (Authenticated Users Only)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can manage orders

# Inventory ViewSet (Admins Only)
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]  # Only admins can manage inventory

# Review ViewSet (Authenticated Users Only)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # Users must be logged in to review products

# Customization ViewSet (Authenticated Users Only)
class CustomizationViewSet(viewsets.ModelViewSet):
    queryset = Customization.objects.all()
    serializer_class = CustomizationSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

# Wishlist ViewSet (Authenticated Users Only)
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

# Promotion ViewSet (Admins Only)
class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  # Only admins can manage promotions

# Order Promotion ViewSet (Authenticated Users Only)
class OrderPromotionViewSet(viewsets.ModelViewSet):
    queryset = OrderPromotion.objects.all()
    serializer_class = OrderPromotionSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can manage order promotions

# Assembly Guide ViewSet (Admins Only)
class AssemblyGuideViewSet(viewsets.ModelViewSet):
    queryset = AssemblyGuide.objects.all()
    serializer_class = AssemblyGuideSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  # Only admins should upload guides

# Home View
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Furniture API! Use /api/ to access the API."})
