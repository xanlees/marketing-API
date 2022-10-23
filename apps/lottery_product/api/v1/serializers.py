
from rest_framework import serializers
from lottery_product.models import Lottery_product


class Lottery_productSerializer(serializers.ModelSerializer):


    class Meta:
        model = Lottery_product
        fields = '__all__'
