from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/buy_lottery', ListCreateAPIView.as_view(), name='buy_lottery'),
    path('api/v1/buy_lottery/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='buy_lottery'),
]
