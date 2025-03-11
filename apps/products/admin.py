from django.contrib import admin
from parler.admin import TranslatableAdmin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Products
from .models import ProductImage
from .models import ProductColorImage
from .models import ProductSizeStock

class ProductsAdmin(TranslatableAdmin, AdminImageMixin):
    list_display = ('name', 'description', 'price', 'image')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'image'),
        }),
    )
    
admin.site.register(Products, ProductsAdmin)

class ProductImages(admin.ModelAdmin):
    list_display = ("product",  "image")
    fieldsets = (
        (None, {"fields": ("product",  "image")}),
    )
    
admin.site.register(ProductImage, ProductImages)


class ProductColorImages(admin.ModelAdmin):
    list_display = ("product", "color_name", "image")
    fieldsets = (
        (None, {"fields": ("product", "color_name", "image")}),
    )
    
admin.site.register(ProductColorImage, ProductColorImages)

class ProductSizeStocks(admin.ModelAdmin):
    list_display = ("product", "size", "stock")
    fieldsets = (
        (None, {"fields": ("product", "size", "stock")}),
    )
    
admin.site.register(ProductSizeStock, ProductSizeStocks)