
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from buy_lottery.models import Buy_Lottery
from .serializers import Buy_Lottery_Serializer


class ListCreateAPIView(ListCreateAPIView):
    queryset = Buy_Lottery.objects.all()
    serializer_class = Buy_Lottery_Serializer

    def get_serializer(self, *args, **kwargs):
        """Allows bulk creation of a resource."""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Buy_Lottery.objects.all()
    serializer_class = Buy_Lottery_Serializer
