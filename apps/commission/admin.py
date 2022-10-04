from django.contrib import admin
from .models import Commission


class CommissionAdmin(admin.ModelAdmin):
    list_display = ('commission','user')
    fieldsets = (
        (None, {
            'fields': ('commission', 'user'),
        }),
    )

admin.site.register(Commission, CommissionAdmin)
