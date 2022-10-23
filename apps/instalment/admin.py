from django.contrib import admin
from .models import Instalment


class InstalementAdmin(admin.ModelAdmin):
    list_display = ('date', 'lottery_day',  'lottery_time')
    fieldsets = (
        (None, {
            'fields': ('date', 'lottery_day',  'lottery_time'),
        }),
    )


admin.site.register(Instalment, InstalementAdmin)
