from django.urls import path
from .views import Predictlose_wingListCreateAPIView, Predictlose_wingRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/predictlose_wing', Predictlose_wingListCreateAPIView.as_view(),name='predictlose_wing'),
    path('api/v1/predictlose_wing/<int:pk>', Predictlose_wingRetrieveUpdateDestroyAPIView.as_view(),name='predictlose_wing'),
]
