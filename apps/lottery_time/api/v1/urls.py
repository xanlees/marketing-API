from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/lottery_time', ListCreateAPIView.as_view(),name='deposit'),
    path('api/v1/lottery_time/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='deposit'),
]