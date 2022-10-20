from django.contrib import admin
from .models import Lottery_day


class Lottery_day_Admin(admin.ModelAdmin):
    list_display = ('days', 'lottery_id')
    fieldsets = (
        (None, {
            'fields': ('days', 'lottery_id'),
        }),
    )


admin.site.register(Lottery_day, Lottery_day_Admin)
