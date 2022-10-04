from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_staff')


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password' )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'])
        return user


class RegisterAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        agent = User.objects.create_user(validated_data['username'],
                                         password=validated_data['password'],
                                         is_staff=validated_data['is_staff'])
        return agent
