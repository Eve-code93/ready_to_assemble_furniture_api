from django.contrib import admin
from .models import (
    User, Furniture, Order, Inventory, Review, 
    Customization, Wishlist, Promotion, OrderPromotion, AssemblyGuide
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'role')
    search_fields = ('username', 'email')

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    list_filter = ('price', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture', 'quantity', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'furniture__name')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'furniture', 'quantity', 'created_at')
    list_filter = ('furniture',)
    search_fields = ('furniture__name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture', 'rating', 'created_at')
    list_filter = ('rating', 'furniture')
    search_fields = ('user__username', 'furniture__name')

@admin.register(Customization)
class CustomizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture', 'customization_details', 'created_at')
    search_fields = ('user__username', 'furniture__name')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'furniture', 'created_at')
    search_fields = ('user__username', 'furniture__name')

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discount_percentage', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)

@admin.register(OrderPromotion)
class OrderPromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'promotion', 'created_at')
    search_fields = ('order__id', 'promotion__name')

@admin.register(AssemblyGuide)
class AssemblyGuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'furniture', 'guide', 'created_at')
    search_fields = ('furniture__name',)
