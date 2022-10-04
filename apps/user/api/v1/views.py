from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


from django.contrib.auth.models import User

from .serializers import UserSerializer, AgentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class ListUserView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        user_serializer = UserSerializer(queryset, many=True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

class RetrieveUserView(APIView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            queryset = User.objects.get(pk=pk)
            if not queryset:
                return Response(
                    {"res": "User id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_serializer = UserSerializer(queryset)

        return Response(user_serializer.data, status=status.HTTP_200_OK)


class ListAgentView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        agent_serializer = AgentSerializer(queryset, many=True)

        return Response(agent_serializer.data, status=status.HTTP_200_OK)

class RetrieveAgentView(APIView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            queryset = User.objects.get(pk=pk)
            if not queryset:
                return Response(
                    {"res": "Agent id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            agent_serializer = AgentSerializer(queryset)

        return Response(agent_serializer.data, status=status.HTTP_200_OK)