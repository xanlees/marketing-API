from django.contrib import admin
from .models import Low_lower, Low_upper, High_lower, High_upper


class Low_lowerAdmin(admin.ModelAdmin):
    list_display = ('name','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('name', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(Low_lower, Low_lowerAdmin)


class Low_upperAdmin(admin.ModelAdmin):
    list_display = ('name','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('name', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(Low_upper, Low_upperAdmin)


class High_lowerAdmin(admin.ModelAdmin):
    list_display = ('name','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('name', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(High_lower, High_lowerAdmin)


class High_upperAdmin(admin.ModelAdmin):
    list_display = ('name','sales', 'win', 'lottery',)
    fieldsets = (
        (None, {
            'fields': ('name', 'sales', 'win', 'lottery',),
        }),
    )

admin.site.register(High_upper, High_upperAdmin)