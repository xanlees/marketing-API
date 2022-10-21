from django.urls import path
from .views import Khus_kickListCreateAPIView, Khus_kickRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/khus_kick', Khus_kickListCreateAPIView.as_view(),name='khus_kick'),
    path('api/v1/khus_kick/<int:pk>', Khus_kickRetrieveUpdateDestroyAPIView.as_view(),name='khus_upper'),
    
]
