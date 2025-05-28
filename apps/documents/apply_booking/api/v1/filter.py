from django_filters import rest_framework as filters
from apps.documents.apply_booking.models import Apply_Booking
from common.constant import CharInFilter, NumberInFilter

class Apply_BookingFilterSet(filters.FilterSet):
    id = NumberInFilter(field_name='id', lookup_expr='in')
    username = CharInFilter(field_name='username', lookup_expr='in')
    date = filters.DateFilter(method='filter_date', label="2024-05-08")
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

    def filter_apply_booking_date(self, queryset, username, value):
        if value:
            queryset = queryset.filter(apply_booking_date=[value])
        return queryset
