
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from cart.models import Cart
from .serializers import CartSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ListCreateAPIView(ListCreateAPIView):
    queryset = Cart.objects.all().order_by("id")
    serializer_class = CartSerializer
    parser_classes = (MultiPartParser, FormParser)

class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    