from django.contrib import admin
from .models import Predictlose_khus_kick


class Predictlose_khus_kickAdmin(admin.ModelAdmin):
    list_display = ('name', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('name', 'instalment'),
        }),
    )


admin.site.register(Predictlose_khus_kick, Predictlose_khus_kickAdmin)



