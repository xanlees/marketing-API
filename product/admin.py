from django.contrib import admin
from parler.admin import TranslatableAdmin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Product


class ProductAdmin(TranslatableAdmin, AdminImageMixin):
    list_display = ('title', 'description', 'slug', 'price', 'image', 'audience')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug', 'price', 'image', 'audience'),
        }),
    )
    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
