from django.urls import path
from .views import Two_lowerListCreateAPIView, Two_lowerRetrieveUpdateDestroyAPIView, Two_upperListCreateAPIView, Two_upperRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/two_lower', Two_lowerListCreateAPIView.as_view(),name='two_lower'),
    path('api/v1/two_lower/<int:pk>', Two_lowerRetrieveUpdateDestroyAPIView.as_view(),name='two_lower'),
    path('api/v1/two_upper', Two_upperListCreateAPIView.as_view(),name='two_upper'),
    path('api/v1/two_upper/<int:pk>', Two_upperRetrieveUpdateDestroyAPIView.as_view(),name='two_upper'),
]
