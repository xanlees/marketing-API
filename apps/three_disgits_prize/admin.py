from django.contrib import admin
from .models import Three_disgits_prize


class Three_disgits_prizeAdmin(admin.ModelAdmin):
    list_display = ('number', 'lottery')
    fieldsets = (
        (None, {
            'fields': ('number', 'lottery'),
        }),
    )

admin.site.register(Three_disgits_prize, Three_disgits_prizeAdmin)
