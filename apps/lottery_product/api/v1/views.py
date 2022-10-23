from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from lottery_product.models import Lottery_product
from .serializers import Lottery_productSerializer

class Lottery_productSerializerListCreateAPIView(ListCreateAPIView):
    queryset = Lottery_product.objects.all()
    serializer_class = Lottery_productSerializer


class Lottery_productSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lottery_product.objects.all()
    serializer_class = Lottery_productSerializer


