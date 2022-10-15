from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from instalment.models import Instalment
from .serializers import InstalmentSerializer


class InstalmentListCreateAPIView(ListCreateAPIView):
    queryset = Instalment.objects.all()
    serializer_class = InstalmentSerializer


class InstalmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Instalment.objects.all()
    serializer_class = InstalmentSerializer


