from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from low_high.models import Low_upper, Low_lower, High_lower, High_upper
from .serializers import Low_lowerSerializer, Low_upperSerializer, High_lowerSerializer, High_upperSerializer


class Low_upperListCreateAPIView(ListCreateAPIView):
    queryset = Low_upper.objects.all()
    serializer_class = Low_upperSerializer


class Low_upperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Low_upper.objects.all()
    serializer_class = Low_upperSerializer


class Low_lowerListCreateAPIView(ListCreateAPIView):
    queryset = Low_lower.objects.all()
    serializer_class = Low_lowerSerializer


class Low_lowerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Low_lower.objects.all()
    serializer_class = Low_lowerSerializer


class High_lowerListCreateAPIView(ListCreateAPIView):
    queryset = High_lower.objects.all()
    serializer_class = High_lowerSerializer


class High_lowerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = High_lower.objects.all()
    serializer_class = High_lowerSerializer


class High_upperListCreateAPIView(ListCreateAPIView):
    queryset = High_upper.objects.all()
    serializer_class = High_upperSerializer


class High_upperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = High_upper.objects.all()
    serializer_class = High_upperSerializer
