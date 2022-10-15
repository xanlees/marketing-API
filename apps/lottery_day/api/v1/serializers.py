from django.conf import settings
from rest_framework import serializers
from lottery_day.models import Lottery_day


class Lottery_daySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_day
        fields = '__all__'
