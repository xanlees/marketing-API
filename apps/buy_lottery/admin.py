from django.contrib import admin
from .models import Buy_Lottery


class Buy_Lottery_Admin(admin.ModelAdmin):
    list_display = ('user', 'number', "amount_buy_top", "amount_buy_bottom")
    fieldsets = (
        (None, {
            'fields': ('user', 'number', "amount_buy_top", "amount_buy_bottom"),
        }),
    )


admin.site.register(Buy_Lottery, Buy_Lottery_Admin)
