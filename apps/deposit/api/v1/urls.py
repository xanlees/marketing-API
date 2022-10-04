from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/deposit', ListCreateAPIView.as_view(),name='deposit'),
    path('api/v1/deposit/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='deposit'),
]