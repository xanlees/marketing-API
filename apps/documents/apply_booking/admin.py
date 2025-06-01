from django.contrib import admin
from .models import Apply_Booking


class Apply_BookingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "phonenumber",
        "email",
        "date",
        "time",
        "document_type",
        "address",
        "status",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "username",
                    "phonenumber",
                    "email",
                    "date",
                    "time",
                    "document_type",
                    "address",
                    "status",
                ]
            },
        )
    ]

admin.site.register(Apply_Booking, Apply_BookingAdmin)
