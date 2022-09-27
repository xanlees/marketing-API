from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/lottery/', ListCreateAPIView.as_view(),name='lottery'),
    path('api/v1/lottery/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='lottery'),
]