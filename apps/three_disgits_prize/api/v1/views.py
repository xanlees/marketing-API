from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from three_disgits_prize.models import Threelower, Threeupper
from .serializers import ThreelowerSerializer, ThreeupperSerializer


class ThreelowerListCreateAPIView(ListCreateAPIView):
    queryset = Threelower.objects.all()
    serializer_class = ThreelowerSerializer


class ThreelowerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Threelower.objects.all()
    serializer_class = ThreelowerSerializer


class ThreeupperListCreateAPIView(ListCreateAPIView):
    queryset = Threeupper.objects.all()
    serializer_class = ThreeupperSerializer


class ThreeupperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Threeupper.objects.all()
    serializer_class = ThreeupperSerializer
