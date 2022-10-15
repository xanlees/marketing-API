
from rest_framework import serializers
from three_disgits_prize.models import Threelower, Threeupper
# from django.utils.module_loading import import_string

# Instalment = import_string('instalment.models.Instalment')


# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['date', 'created_on']


class ThreelowerSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Threelower
        fields = '__all__'

class ThreeupperSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Threeupper
        fields = '__all__'