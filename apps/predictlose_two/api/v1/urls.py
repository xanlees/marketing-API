from django.urls import path
from .views import Predictlose_twoSerializerListCreateAPIView, Predictlose_twoSerializerRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/predictlose_two', Predictlose_twoSerializerListCreateAPIView.as_view(),name='predictlose_two'),
    path('api/v1/predictlose_two/<int:pk>', Predictlose_twoSerializerRetrieveUpdateDestroyAPIView.as_view(),name='predictlose_two'),
]
