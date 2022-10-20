from django.contrib import admin
from .models import Two_disgits_prize


class Two_disgits_prizeAdmin(admin.ModelAdmin):
    list_display = ('number', 'lottery')
    fieldsets = (
        (None, {
            'fields': ('number', 'lottery'),
        }),
    )


admin.site.register(Two_disgits_prize, Two_disgits_prizeAdmin)
