from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.documents.apply_booking.api.v1.serializers import Apply_BookingSerializer
from apps.documents.apply_booking.models import Apply_Booking
from .filter import Apply_BookingFilterSet


class Apply_BookingListCreateAPIView(ListCreateAPIView):
    queryset = Apply_Booking.objects.all()
    serializer_class = Apply_BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Apply_BookingFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

class Apply_BookingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Apply_Booking.objects.all()
    serializer_class = Apply_BookingSerializer
