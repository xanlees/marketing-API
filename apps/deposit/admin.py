from django.contrib import admin
from .models import Deposit


class DepositAdmin(admin.ModelAdmin):
    list_display = ('deposit_amout','user')
    fieldsets = (
        (None, {
            'fields': ('deposit_amout', 'user'),
        }),
    )

admin.site.register(Deposit, DepositAdmin)
