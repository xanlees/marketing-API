from django.urls import path
from .views import (
    Apply_BookingListCreateAPIView,
    Apply_BookingRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path(
        "api/v1/apply_booking",
        Apply_BookingListCreateAPIView.as_view(),
        name="apply_booking",
    ),
    path(
        "api/v1/apply_booking/<int:pk>",
        Apply_BookingRetrieveUpdateDestroyAPIView.as_view(),
        name="apply_booking",
    ),
]

