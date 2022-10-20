from django.contrib import admin
from .models import Low_high


class Low_lowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lottery', )
    fieldsets = (
        (None, {
            'fields': ('name', 'lottery', ),
        }),
    )

admin.site.register(Low_high, Low_lowerAdmin)


