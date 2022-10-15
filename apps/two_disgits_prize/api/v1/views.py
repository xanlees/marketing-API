from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from two_disgits_prize.models import Two_lower, Two_upper
from .serializers import Two_lowerSerializer, Two_upperSerializer


class Two_lowerListCreateAPIView(ListCreateAPIView):
    queryset = Two_lower.objects.all()
    serializer_class = Two_lowerSerializer


class Two_lowerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Two_lower.objects.all()
    serializer_class = Two_lowerSerializer


class Two_upperListCreateAPIView(ListCreateAPIView):
    queryset = Two_upper.objects.all()
    serializer_class = Two_upperSerializer


class Two_upperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Two_upper.objects.all()
    serializer_class = Two_upperSerializer
