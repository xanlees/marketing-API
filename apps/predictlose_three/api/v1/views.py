from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from predictlose_three.models import Predictlose_three
from .serializers import Predictlose_threeSerializer


class Predictlose_threeListCreateAPIView(ListCreateAPIView):
    queryset = Predictlose_three.objects.all()
    serializer_class = Predictlose_threeSerializer


class Predictlose_threeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Predictlose_three.objects.all()
    serializer_class = Predictlose_threeSerializer



