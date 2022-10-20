from django.urls import path
from .views import Three_disgits_prizeListCreateAPIView, Three_disgits_prizeRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/three_disgits_prize', Three_disgits_prizeListCreateAPIView.as_view(),name='three_disgits_prize'),
    path('api/v1/three_disgits_prize/<int:pk>', Three_disgits_prizeRetrieveUpdateDestroyAPIView.as_view(),name='three_disgits_prize'),
]
