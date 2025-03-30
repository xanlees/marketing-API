from django.urls import path, include
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ReduceStockAPIView, MensShoesListAPIView, WomensShoesListAPIView, KidsListAPIView, JorDanAllListAPIView, SportAllListAPIView
urlpatterns = [
    path('api/v1/products/', ListCreateAPIView.as_view(),name='products'),
    path('api/v1/products/mens/', MensShoesListAPIView.as_view(), name='mens-shoes'),
    path('api/v1/products/womens/', WomensShoesListAPIView.as_view(), name='womens-shoes'),
    path('api/v1/products/kids/', KidsListAPIView.as_view(), name='kids-shoes'),
    path('api/v1/products/jor-dan/', JorDanAllListAPIView.as_view(), name='jor-dan-shoes'),
    path('api/v1/products/sports/', SportAllListAPIView.as_view(), name='sports-shoes'),
    path('api/v1/products/<str:id>/', RetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),   
    path('api/v1/products/<str:product_id>/reduce_stock/', ReduceStockAPIView.as_view(), name='reduce_stock'),  # ✅ New stock update URL
]