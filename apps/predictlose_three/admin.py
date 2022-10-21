from django.contrib import admin
from .models import Predictlose_three


class Predictlose_threeAdmin(admin.ModelAdmin):
    list_display = ('number', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('number', 'instalment'),
        }),
    )

admin.site.register(Predictlose_three, Predictlose_threeAdmin)
