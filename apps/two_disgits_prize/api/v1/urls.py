from django.urls import path
from .views import Two_lowerListCreateAPIView, Two_lowerRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/two_disgits_prize', Two_lowerListCreateAPIView.as_view(),name='two_disgits_prize'),
    path('api/v1/two_disgits_prize/<int:pk>', Two_lowerRetrieveUpdateDestroyAPIView.as_view(),name='two_disgits_prize'),
]
