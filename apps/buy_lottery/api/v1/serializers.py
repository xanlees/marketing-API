from django.conf import settings
from rest_framework import serializers
from buy_lottery.models import Buy_Lottery


class Buy_Lottery_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Buy_Lottery
        fields = '__all__'
