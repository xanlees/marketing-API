from django.conf import settings
from rest_framework import serializers
from deposit.models import Deposit


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
