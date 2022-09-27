
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from lottery.models import Lottery
from .serializers import LotterySerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ListCreateAPIView(ListCreateAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
    parser_classes = (MultiPartParser, FormParser)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lottery.objects.all()
    serializer_class = LotterySerializer
    parser_classes = (MultiPartParser, FormParser)