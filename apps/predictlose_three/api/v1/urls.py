from django.urls import path
from .views import Predictlose_threeListCreateAPIView, Predictlose_threeRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/predictlose_three', Predictlose_threeListCreateAPIView.as_view(),name='predictlose_three'),
    path('api/v1/predictlose_three/<int:pk>', Predictlose_threeRetrieveUpdateDestroyAPIView.as_view(),name='predictlose_three'),
]
