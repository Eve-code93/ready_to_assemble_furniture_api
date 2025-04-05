from django.contrib import admin
from .models import (
    User, Furniture, Order, Inventory, Review, 
    Customization, Wishlist, Promotion, OrderPromotion, AssemblyGuide
)

# Register the models to the admin interface with customization

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')  # Customize fields for display
    search_fields = ('username', 'email')  # Enable search functionality

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')  # Customize fields for display
    list_filter = ('category', 'price')  # Add filters
    search_fields = ('name', 'description')  # Enable search functionality

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status')  # Customize fields for display
    list_filter = ('status', 'created_at')  # Add filters
    search_fields = ('user__username', 'status')  # Enable search by related user

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'furniture', 'quantity')  # Display fields
    list_filter = ('furniture',)  # Add filters
    search_fields = ('furniture__name',)  # Enable search by furniture name

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture', 'rating')  # Display fields
    list_filter = ('rating', 'furniture')  # Add filters
    search_fields = ('user__username', 'furniture__name')  # Enable search

@admin.register(Customization)
class CustomizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture', 'options')  # Display fields
    search_fields = ('user__username', 'furniture__name')  # Enable search

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture')  # Display fields
    search_fields = ('user__username', 'furniture__name')  # Enable search

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'discount', 'active')  # Display fields
    list_filter = ('active',)  # Filter by active status
    search_fields = ('title',)  # Enable search

@admin.register(OrderPromotion)
class OrderPromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'promotion')  # Display fields
    search_fields = ('order__id', 'promotion__title')  # Enable search

@admin.register(AssemblyGuide)
class AssemblyGuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'furniture', 'file')  # Display fields
    search_fields = ('furniture__name',)  # Enable search
