from django.conf import settings
from rest_framework import serializers
from lottery_time.models import Lottery_time


class Lottery_time_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_time
        fields = '__all__'

