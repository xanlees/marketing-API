from django.urls import path
from .views import Lottery_productSerializerListCreateAPIView, Lottery_productSerializerRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/lottery_product', Lottery_productSerializerListCreateAPIView.as_view(),name='lottery_product'),
    path('api/v1/lottery_product/<int:pk>', Lottery_productSerializerRetrieveUpdateDestroyAPIView.as_view(),name='lottery_product'),
]
