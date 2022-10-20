from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from three_disgits_prize.models import Three_disgits_prize
from .serializers import Three_disgits_prizeSerializer


class Three_disgits_prizeListCreateAPIView(ListCreateAPIView):
    queryset = Three_disgits_prize.objects.all()
    serializer_class = Three_disgits_prizeSerializer


class Three_disgits_prizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Three_disgits_prize.objects.all()
    serializer_class = Three_disgits_prizeSerializer



