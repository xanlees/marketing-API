from django.contrib import admin
from .models import Lottery_time


class Lottery_time_Admin(admin.ModelAdmin):
    list_display = ('lottery_day', 'open_date', 'closing_date')
    fieldsets = (
        (None, {
            'fields': ('lottery_day', 'open_date', 'closing_date'),
        }),
    )


admin.site.register(Lottery_time, Lottery_time_Admin)
