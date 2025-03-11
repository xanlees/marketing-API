from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from products.models import Products, ProductImage
from .serializers import ProductSerializer
from django.db.models import F
import json


class ProductImageViewSet(ListCreateAPIView):
    queryset = ProductImage.objects.all().order_by("id")
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)



class ListCreateAPIView(ListCreateAPIView):
    queryset = Products.objects.all().order_by("id")
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)


class ReduceStockAPIView(APIView):
    def patch(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)

        size = request.data.get("size")
        quantity = request.data.get("quantity")

        # ✅ Ensure `sizes` is a dictionary
        if not isinstance(product.sizes, dict):
            return Response({"error": "Invalid product sizes format"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Validate size exists in sizes dictionary
        if not size or size not in product.sizes:
            return Response({"error": "Invalid size selection"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Validate quantity is a positive integer
        try:
            quantity = int(quantity)
        except ValueError:
            return Response({"error": "Quantity must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        if quantity <= 0:
            return Response({"error": "Invalid quantity value"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Check if enough stock is available for that size
        if product.sizes[size] < quantity:
            return Response({"error": "Not enough stock available"}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Reduce stock for selected size
        product.sizes[size] -= quantity
        product.save(update_fields=["sizes"]) # ✅ Save only the sizes field

        return Response({
            "message": "Stock updated successfully",
            "new_stock": json.loads(product.sizes)  # ✅ Ensure proper JSON format in response
        }, status=status.HTTP_200_OK)