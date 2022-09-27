from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializations import RateSerializer
from djmoney.contrib.exchange.models import Rate


class ListRateAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class RetrieveUpdateDestroyRateAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

