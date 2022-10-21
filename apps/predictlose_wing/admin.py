from django.contrib import admin
from .models import Predictlose_wing


class Predictlose_wingAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    fieldsets = (
        (None, {
            'fields': ('name', 'number'),
        }),
    )
  
admin.site.register(Predictlose_wing, Predictlose_wingAdmin)


