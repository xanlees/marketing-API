from rest_flex_fields import FlexFieldsModelSerializer
from apps.documents.apply_booking.models import Apply_Booking


class Apply_BookingSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Apply_Booking
        fields = [
            "id",
            "username",
            "phonenumber",
            "email",
            "date",
            "time",
            "document_type",
            "address",
        ]

