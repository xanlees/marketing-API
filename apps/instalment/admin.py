from django.contrib import admin
from .models import Instalment


class InstalementAdmin(admin.ModelAdmin):
    list_display = ('date', 'lottery')
    fieldsets = (
        (None, {
            'fields': ('date', 'lottery'),
        }),
    )

admin.site.register(Instalment, InstalementAdmin)
