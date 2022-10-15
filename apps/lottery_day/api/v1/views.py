
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import Lottery_daySerializer
from lottery_day.models import Lottery_day


class ListCreateAPIView(ListCreateAPIView):
    queryset = Lottery_day.objects.all()
    serializer_class = Lottery_daySerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lottery_day.objects.all()
    serializer_class = Lottery_daySerializer
