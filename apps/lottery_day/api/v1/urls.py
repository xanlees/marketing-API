from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/lottery_day', ListCreateAPIView.as_view(), name='lottery_day'),
    path('api/v1/lottery_day/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='lottery_day'),
]
