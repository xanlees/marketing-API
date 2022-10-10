from dataclasses import field
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.module_loading import import_string

Deposit = import_string('deposit.models.Deposit')
Commission = import_string('commission.models.Commission')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class DepositAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['deposit_amount', 'updated_on']

class CommissionssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['commission', 'updated_on']

class UserSerializer(serializers.ModelSerializer):
    deposit = DepositAmountSerializer(many=True, read_only=True)
    commission = CommissionssSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'is_active', 'is_staff','date_joined', 'deposit', 'commission')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password', 'is_active')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password = validated_data['password'],
                                        is_active = validated_data['is_active'])
        return user

class RegisterStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password', 'is_active', 'is_staff')
        extra_kwargs = {
            'password':{'write_only': True},
            
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password = validated_data['password'],
                                        is_active = validated_data['is_active'],
                                        is_staff = validated_data['is_staff'])
        return user