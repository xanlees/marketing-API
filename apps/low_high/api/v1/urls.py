from django.urls import path
from .views import Low_lowerListCreateAPIView, Low_lowerRetrieveUpdateDestroyAPIView, Low_upperListCreateAPIView, Low_upperRetrieveUpdateDestroyAPIView, High_lowerListCreateAPIView, High_lowerRetrieveUpdateDestroyAPIView, High_upperListCreateAPIView, High_upperRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/low_lower', Low_lowerListCreateAPIView.as_view(),name='low_lower'),
    path('api/v1/low_lower/<int:pk>', Low_lowerRetrieveUpdateDestroyAPIView.as_view(),name='low_lower'),
    path('api/v1/low_upper', Low_upperListCreateAPIView.as_view(),name='low_upper'),
    path('api/v1/low_upper/<int:pk>', Low_upperRetrieveUpdateDestroyAPIView.as_view(),name='low_upper'),
    path('api/v1/high_lower', High_lowerListCreateAPIView.as_view(),name='high_lower'),
    path('api/v1/high_lower/<int:pk>', High_lowerRetrieveUpdateDestroyAPIView.as_view(),name='high_lower'),
    path('api/v1/high_upper', High_upperListCreateAPIView.as_view(),name='high_upper'),
    path('api/v1/high_upper/<int:pk>', High_upperRetrieveUpdateDestroyAPIView.as_view(),name='high_upper'),
]
