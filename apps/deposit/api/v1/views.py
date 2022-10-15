from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from deposit.models import Deposit
from .serializers import DepositSerializer

class ListCreateAPIView(ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer



class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer