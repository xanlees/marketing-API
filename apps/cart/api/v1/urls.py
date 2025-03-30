from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/cart', ListCreateAPIView.as_view(),name='cart'),
    path('api/v1/cart/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='cart'),
    
]