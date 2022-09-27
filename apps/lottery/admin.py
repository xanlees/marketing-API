from django.contrib import admin
from parler.admin import TranslatableAdmin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Lottery


class LotteryAdmin(TranslatableAdmin, AdminImageMixin):
    list_display = ('name','open_date', 'closing_date', 'image')
    fieldsets = (
        (None, {
            'fields': ('name', 'open_date', 'closing_date', 'image'),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super().save_model(request, obj, form, change)

admin.site.register(Lottery, LotteryAdmin)
