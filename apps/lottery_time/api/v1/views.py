
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from lottery_time.models import Lottery_time
from .serializers import Lottery_time_Serializer

class ListCreateAPIView(ListCreateAPIView):
    queryset = Lottery_time.objects.all()
    serializer_class = Lottery_time_Serializer

    
class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lottery_time.objects.all()
    serializer_class = Lottery_time_Serializer