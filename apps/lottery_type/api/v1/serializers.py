from django.conf import settings
from rest_framework import serializers
from lottery_type.models import Lottery_type


class Lottery_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_type
        fields = '__all__'

