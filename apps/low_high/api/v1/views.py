from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from low_high.models import Low_high
from .serializers import Low_highSerializer


class Low_upperListCreateAPIView(ListCreateAPIView):
    queryset = Low_high.objects.all()
    serializer_class = Low_highSerializer


class Low_upperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Low_high.objects.all()
    serializer_class = Low_highSerializer


