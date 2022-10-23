from django.contrib import admin
from .models import Lottery_type


class Lottery_type_Admin(admin.ModelAdmin):
    list_display = ('type', 'mutiple')
    fieldsets = (
        (None, {
            'fields': ('type', 'mutiple'),
        }),
    )


admin.site.register(Lottery_type, Lottery_type_Admin)
