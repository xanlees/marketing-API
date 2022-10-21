from django.urls import path
from .views import Predictlose_low_highListCreateAPIView, Predictlose_low_highRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/predictlose_low_high', Predictlose_low_highListCreateAPIView.as_view(),name='predictlose_low_high'),
    path('api/v1/predictlose_low_high/<int:pk>', Predictlose_low_highRetrieveUpdateDestroyAPIView.as_view(),name='predictlose_low_high'),
]
