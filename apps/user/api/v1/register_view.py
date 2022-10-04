from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterStaffSerializer, AgentSerializer


class RegisterUserSerializerView(generics.GenericAPIView):
    serializer_class = AgentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })

class RegisterStaffView(generics.GenericAPIView):
    serializer_class = RegisterStaffSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })