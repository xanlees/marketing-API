
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import Lottery_daySerializer
from lottery_day.models import Lottery_day


class ListCreateAPIView(ListCreateAPIView):
    queryset = Lottery_day.objects.all()
    serializer_class = Lottery_daySerializer

    def get_serializer(self, *args, **kwargs):
        """Allows bulk creation of a resource."""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lottery_day.objects.all()
    serializer_class = Lottery_daySerializer
