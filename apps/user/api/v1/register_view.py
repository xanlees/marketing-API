from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, RegisterAgentSerializer, UserSerializer


class RegisterUserSerializerView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })

class RegisterAgentSerializerView(generics.GenericAPIView):
    serializer_class = RegisterAgentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        agent = serializer.save()
        return Response({
            "agent": UserSerializer(agent, context=self.get_serializer_context()).data
        })