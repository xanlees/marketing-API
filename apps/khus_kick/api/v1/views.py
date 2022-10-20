from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from khus_kick.models import Khus_kick
from .serializers import Khus_kickSerializer


class Khus_kickListCreateAPIView(ListCreateAPIView):
    queryset = Khus_kick.objects.all()
    serializer_class = Khus_kickSerializer


class Khus_kickRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Khus_kick.objects.all()
    serializer_class = Khus_kickSerializer



