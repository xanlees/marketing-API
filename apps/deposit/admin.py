from django.contrib import admin
from .models import Deposit


class DepositAdmin(admin.ModelAdmin):
    list_display = ('deposit_amount','user')
    fieldsets = (
        (None, {
            'fields': ('deposit_amount', 'user'),
        }),
    )

admin.site.register(Deposit, DepositAdmin)
