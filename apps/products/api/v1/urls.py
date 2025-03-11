from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ReduceStockAPIView, ProductImageViewSet

urlpatterns = [
    path('api/v1/products', ListCreateAPIView.as_view(),name='products'),
    path('api/v1/products/<int:pk>', RetrieveUpdateDestroyAPIView.as_view(),name='products'),
    path('api/v1/product_images/<int:pk>/images', ProductImageViewSet.as_view(), name='product_images'),  # ✅ New image handling URL   
    path('api/v1/products/<int:product_id>/reduce_stock/', ReduceStockAPIView.as_view(), name='reduce_stock'),  # ✅ New stock update URL
]