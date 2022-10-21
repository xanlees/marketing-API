from django.contrib import admin
from .models import Predictlose_wing


class Predictlose_wingAdmin(admin.ModelAdmin):
    list_display = ('number','instalment')
    fieldsets = (
        (None, {
            'fields': ('number','instalment'),
        }),
    )
  
admin.site.register(Predictlose_wing, Predictlose_wingAdmin)


