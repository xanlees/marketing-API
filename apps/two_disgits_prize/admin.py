from django.contrib import admin
from .models import Two_lower, Two_upper


class Two_lowerAdmin(admin.ModelAdmin):
    list_display = ('number','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('number', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(Two_lower, Two_lowerAdmin)


class Two_upperAdmin(admin.ModelAdmin):
    list_display = ('number','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('number', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(Two_upper, Two_upperAdmin)