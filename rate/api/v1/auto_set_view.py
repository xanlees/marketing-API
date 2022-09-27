from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .auto_set_serializations import AutoSetSerializer



class AutoSetView(generics.GenericAPIView):
    serializer_class = AutoSetSerializer

    def post(self, request, *args, **kwargs):
        try:
            AutoSetSerializer.create(self)
            return Response({'message': 'Update rate successfully'}, status=status.HTTP_201_CREATED)
        except:
            return  Response({'message': 'Failed to update rate'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)