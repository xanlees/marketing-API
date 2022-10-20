from django.contrib import admin
from .models import Khus_kick


class Khus_kickAdmin(admin.ModelAdmin):
    list_display = ('name', 'lottery', 'instalment')
    fieldsets = (
        (None, {
            'fields': ('name', 'lottery', 'instalment'),
        }),
    )


admin.site.register(Khus_kick, Khus_kickAdmin)



