from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """set up the customised admin panel for products"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """set up admin panel for categories"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
