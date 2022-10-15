from django.urls import path
from .views import InstalmentListCreateAPIView, InstalmentRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/instalment', InstalmentListCreateAPIView.as_view(),name='instalment'),
    path('api/v1/instalment/<int:pk>', InstalmentRetrieveUpdateDestroyAPIView.as_view(),name='instalment'),
]
