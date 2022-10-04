from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


from django.contrib.auth.models import User

from .serializers import UserSerializer, AgentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class ListUserView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        is_staff = self.request.query_params.get('is_staff')
        if is_staff is not None:
            queryset = queryset.filter(is_staff=is_staff)
        return queryset


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
