from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from predictlose_wing.models import Predictlose_wing
from .serializers import Predictlose_wingSerializer


class Predictlose_wingListCreateAPIView(ListCreateAPIView):
    queryset = Predictlose_wing.objects.all()
    serializer_class = Predictlose_wingSerializer


class Predictlose_wingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Predictlose_wing.objects.all()
    serializer_class = Predictlose_wingSerializer


