from django.contrib import admin
from .models import Lottery_day


class Lottery_day_Admin(admin.ModelAdmin):
    list_display = ('days', 'lottery')
    fieldsets = (
        (None, {
            'fields': ('days', 'lottery'),
        }),
    )


admin.site.register(Lottery_day, Lottery_day_Admin)
