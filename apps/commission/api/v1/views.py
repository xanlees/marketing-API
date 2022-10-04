
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from commission.models import Commission
from .serializers import CommissionSerializer

class ListCreateAPIView(ListCreateAPIView):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer