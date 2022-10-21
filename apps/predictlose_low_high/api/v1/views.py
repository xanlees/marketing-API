from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from predictlose_low_high.models import Predictlose_low_high
from .serializers import Predictlose_low_highSerializer


class Predictlose_low_highListCreateAPIView(ListCreateAPIView):
    queryset = Predictlose_low_high.objects.all()
    serializer_class = Predictlose_low_highSerializer


class Predictlose_low_highRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Predictlose_low_high.objects.all()
    serializer_class = Predictlose_low_highSerializer


