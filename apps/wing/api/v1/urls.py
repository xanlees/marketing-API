from django.urls import path
from .views import WingListCreateAPIView, WingRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/wing', WingListCreateAPIView.as_view(),name='wing'),
    path('api/v1/wing/<int:pk>', WingRetrieveUpdateDestroyAPIView.as_view(),name='wing'),
]
