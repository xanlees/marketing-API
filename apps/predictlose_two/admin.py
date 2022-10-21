from django.contrib import admin
from .models import Predictlose_two


class Predictlose_twoAdmin(admin.ModelAdmin):
    list_display = ('number', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('number', 'instalment'),
        }),
    )


admin.site.register(Predictlose_two, Predictlose_twoAdmin)
