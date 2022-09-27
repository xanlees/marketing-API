from django.urls import path
from .views import ListRateAPIView, RetrieveUpdateDestroyRateAPIView
from .auto_set_view import AutoSetView

urlpatterns = [
    path("api/v1/rate/",ListRateAPIView.as_view(),name="rate"),
    path("api/v1/rate/<pk>",RetrieveUpdateDestroyRateAPIView.as_view(),name="rate"),
    path('api/v1/rate/auto_set/', AutoSetView.as_view(), name='auto_set')
]