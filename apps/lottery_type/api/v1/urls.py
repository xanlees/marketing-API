from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/lottery_type', ListCreateAPIView.as_view(),name='lottery_type'),
    path('api/v1/lottery_type/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='lottery_type'),
]