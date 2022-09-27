
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import Product
from .serializers import ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)