from rest_framework import serializers
from .models import (
    User, Furniture, Order, Inventory, Review, 
    Customization, Wishlist, Promotion, OrderPromotion, AssemblyGuide
)

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'created_at']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Furniture Serializer
class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['id', 'name', 'description', 'price', 'created_at']

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'user', 'furniture', 'quantity', 'total_price', 'created_at']

# Inventory Serializer
class InventorySerializer(serializers.ModelSerializer):
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = Inventory
        fields = ['id', 'furniture', 'quantity', 'created_at']

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'furniture', 'rating', 'comment', 'created_at']

# Customization Serializer
class CustomizationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = Customization
        fields = ['id', 'user', 'furniture', 'customization_details', 'created_at']

# Wishlist Serializer
class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'furniture', 'created_at']

# Promotion Serializer
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'discount_percentage', 'created_at']

# Order Promotion Serializer
class OrderPromotionSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    promotion = serializers.PrimaryKeyRelatedField(queryset=Promotion.objects.all())

    class Meta:
        model = OrderPromotion
        fields = ['id', 'order', 'promotion', 'created_at']

# Assembly Guide Serializer
class AssemblyGuideSerializer(serializers.ModelSerializer):
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = AssemblyGuide
        fields = ['id', 'furniture', 'guide', 'created_at']
