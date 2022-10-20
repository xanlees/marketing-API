from django.urls import path
from .views import Low_upperListCreateAPIView, Low_upperRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/low_high', Low_upperListCreateAPIView.as_view(),name='low_high'),
    path('api/v1/low_high/<int:pk>', Low_upperRetrieveUpdateDestroyAPIView.as_view(),name='low_high'),
]
