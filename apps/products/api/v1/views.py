from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from products.models import Products, ProductImage, ProductSizeStock
from .serializers import ProductSerializer, ColorImageSerializer
from django.db.models import F
import json
from rest_framework.generics import ListAPIView


class ListCreateAPIView(ListCreateAPIView):
    queryset = Products.objects.prefetch_related(
        'color_images__stock_sizes'
    ).all().order_by('id')
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
         
class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    parser_classes = (MultiPartParser, FormParser)


class ReduceStockAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def patch(self, request, product_id):
        
          
        product = get_object_or_404(Products, id=product_id)
        
        color_name = request.data.get("color_name")
        size = request.data.get("size")
        quantity = request.data.get("quantity")


        if not color_name or not size or not quantity:
            return Response(
                {"error": "Color, size, and quantity are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError()
        except ValueError:
            return Response(
                {"error": "Quantity must be a positive integer."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        color_images = product.color_images.filter(color_name__iexact=color_name).first()
        
        if not color_images:
            return Response({"error": "Size not found."},
                            status=status.HTTP_404_NOT_FOUND)
            
        stock_size = color_images.stock_sizes.filter(size=size).first()
        
        if not stock_size:
            return Response({"error": "Size not found."}, status=status.HTTP_404_NOT_FOUND)
         
        if stock_size.stock < quantity:
            return Response({"error": "Insufficient stock."},
                            status=status.HTTP_400_BAD_REQUEST)
            
        # ✅ Reduce stock for selected size
        stock_size.stock -= quantity
        stock_size.save(update_fields=['stock']) # ✅ Save only the sizes field

        return Response({
            "message": "Stock updated successfully",
            "new_stock": {
                "color": color_name,
                "size": size,
                "remaining_stock": stock_size.stock
            }
        }, status=status.HTTP_200_OK)


class MensShoesListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(type="Men")

class WomensShoesListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(type="Women")
    
class KidsListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(type="Kids")
    
class JorDanListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(type="JorDan")
    
class SportAllListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(category__name="Sport's Shoes")
    
class JorDanAllListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(category__name="Jordan's Shoes")