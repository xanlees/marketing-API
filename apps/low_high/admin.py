from django.contrib import admin
from .models import Low_high


class Low_lowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lottery', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('name', 'lottery', 'instalment'),
        }),
    )

admin.site.register(Low_high, Low_lowerAdmin)


