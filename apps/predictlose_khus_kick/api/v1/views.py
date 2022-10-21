from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from predictlose_khus_kick.models import Predictlose_khus_kick
from .serializers import Khus_kickSerializer


class Khus_kickListCreateAPIView(ListCreateAPIView):
    queryset = Predictlose_khus_kick.objects.all()
    serializer_class = Khus_kickSerializer


class Khus_kickRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Predictlose_khus_kick.objects.all()
    serializer_class = Khus_kickSerializer



