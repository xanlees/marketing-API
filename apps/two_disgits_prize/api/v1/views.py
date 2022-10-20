from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from two_disgits_prize.models import Two_disgits_prize
from .serializers import Two_disgits_prizeSerializer

class Two_lowerListCreateAPIView(ListCreateAPIView):
    queryset = Two_disgits_prize.objects.all()
    serializer_class = Two_disgits_prizeSerializer


class Two_lowerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Two_disgits_prize.objects.all()
    serializer_class = Two_disgits_prizeSerializer


