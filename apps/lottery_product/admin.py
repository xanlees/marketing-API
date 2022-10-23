from django.contrib import admin
from .models import Lottery_product


class Lottery_productAdmin(admin.ModelAdmin):
    list_display = ('lottery_name', 'status', 'limitcost', 'lottery_type' )
    fieldsets = (
        (None, {
            'fields': ('lottery_name', 'status', 'limitcost', 'lottery_type' ),
        }),
    )


admin.site.register(Lottery_product, Lottery_productAdmin)
