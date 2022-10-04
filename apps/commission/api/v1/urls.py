from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/commission', ListCreateAPIView.as_view(),name='commission'),
    path('api/v1/commission/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='commission'),
]