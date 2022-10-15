from django.urls import path
from .views import ThreelowerListCreateAPIView, ThreelowerRetrieveUpdateDestroyAPIView, ThreeupperListCreateAPIView, ThreeupperRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/three_lower', ThreelowerListCreateAPIView.as_view(),name='three_lower'),
    path('api/v1/three_lower/<int:pk>', ThreelowerRetrieveUpdateDestroyAPIView.as_view(),name='three_lower'),
    path('api/v1/three_upper', ThreeupperListCreateAPIView.as_view(),name='three_upper'),
    path('api/v1/three_upper/<int:pk>', ThreeupperRetrieveUpdateDestroyAPIView.as_view(),name='three_upper'),
]
