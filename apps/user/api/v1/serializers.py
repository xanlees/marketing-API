from dataclasses import field
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.module_loading import import_string
from django.contrib.auth import authenticate

Deposit = import_string('deposit.models.Deposit')
Commission = import_string('commission.models.Commission')
# Instalment = import_string('instalment.models.Instalment')
# Balance = import_string('balance.models.Balance')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
      def validate(self, attrs):
            # Get the username and password
        username = attrs.get("username")  # We are now using the username instead of email
        password = attrs.get("password")

        # Authenticate the user with the username and password
        user = authenticate(username=username, password=password)

        # If authentication fails, raise a validation error
        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        # Generate the token with the additional username claim
        token = super(MyTokenObtainPairSerializer, self).validate(attrs)
        token['username'] = user.username  # Add the custom 'username' claim to the token
        
        return token
        

class DepositAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['deposit_amount', 'updated_on']

class CommissionssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['commission', 'updated_on']

# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['date', 'created_on']
        
# class BalanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Balance
#         fields = ['balance', 'created_on']

class UserSerializer(serializers.ModelSerializer):
    deposit = DepositAmountSerializer(many=True, read_only=True)
    commission = CommissionssSerializer(many=True, read_only=True)
    # instalment = InstalmentSerializer(many=True, read_only=True)
    # balance = BalanceSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'is_active', 'is_staff','date_joined', 'commission','deposit', )

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
                                        is_staff = validated_data['is_staff'],
                                        )
        return user
    
    