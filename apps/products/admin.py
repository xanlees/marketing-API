from django.contrib import admin
from parler.admin import TranslatableAdmin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Products
from .models import ProductImage
from .models import ProductColorImage
from .models import ProductSizeStock
from .models import Category


class CategoryInline(AdminImageMixin, admin.TabularInline):
    model = Category
    extra = 1

class ProductImageInline(AdminImageMixin, admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductColorImageInline(AdminImageMixin, admin.TabularInline):
    model = ProductColorImage
    extra = 1

class ProductSizeStockInline(admin.TabularInline):
    model = ProductSizeStock
    extra = 1

@admin.register(Products)
class ProductsAdmin(AdminImageMixin, TranslatableAdmin):
    list_display = ('id','name', 'description', 'type', 'price')
    search_fields = ('name',)
    inlines = [ ProductColorImageInline, ProductImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product__name',)

@admin.register(ProductColorImage)
class ProductColorImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('product', 'color_name', 'image')
    inlines = [ ProductSizeStockInline]

@admin.register(ProductSizeStock)
class ProductSizeStockAdmin(admin.ModelAdmin):
    list_display = ( 'color_image','size', 'stock')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)