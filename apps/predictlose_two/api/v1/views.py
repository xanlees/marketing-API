from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from predictlose_two.models import Predictlose_two
from .serializers import Predictlose_twoSerializer

class Predictlose_twoSerializerListCreateAPIView(ListCreateAPIView):
    queryset = Predictlose_two.objects.all()
    serializer_class = Predictlose_twoSerializer


class Predictlose_twoSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Predictlose_two.objects.all()
    serializer_class = Predictlose_twoSerializer


