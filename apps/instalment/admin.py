from django.contrib import admin
from .models import Instalment


class InstalementAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'lottery_time')
    fieldsets = (
        (None, {
            'fields': ('created_on', 'lottery_time'),
        }),
    )

admin.site.register(Instalment, InstalementAdmin)
