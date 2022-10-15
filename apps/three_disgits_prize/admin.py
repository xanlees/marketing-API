from django.contrib import admin
from .models import Threelower, Threeupper


class ThreelowerAdmin(admin.ModelAdmin):
    list_display = ('number','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('number', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(Threelower, ThreelowerAdmin)


class ThreeupperAdmin(admin.ModelAdmin):
    list_display = ('number','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('number', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(Threeupper, ThreelowerAdmin)