from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/product/', ListCreateAPIView.as_view(),name='product'),
    path('api/v1/product/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='product'),
]