from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'image',  'size', 'color', 'price', 'quantity')
    fieldsets = (
        (None, {
            'fields': ('product_id', 'image', 'size', 'color', 'price', 'quantity'),
        }),
    )
    
admin.site.register(Cart, CartAdmin)