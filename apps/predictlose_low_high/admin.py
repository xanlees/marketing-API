from django.contrib import admin
from .models import Predictlose_low_high


class Predictlose_low_highAdmin(admin.ModelAdmin):
    list_display = ('name', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('name', 'instalment'),
        }),
    )

admin.site.register(Predictlose_low_high, Predictlose_low_highAdmin)


