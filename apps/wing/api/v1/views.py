from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from wing.models import Wing
from .serializers import WingSerializer


class WingListCreateAPIView(ListCreateAPIView):
    queryset = Wing.objects.all()
    serializer_class = WingSerializer


class WingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Wing.objects.all()
    serializer_class = WingSerializer


