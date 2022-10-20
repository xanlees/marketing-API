from django.contrib import admin
from .models import Wing


class Wing_upperAdmin(admin.ModelAdmin):
    list_display = ('number','lottery', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('number','lottery', 'instalment'),
        }),
    )
  
admin.site.register(Wing, Wing_upperAdmin)


