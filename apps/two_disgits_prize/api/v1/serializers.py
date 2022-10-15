
from rest_framework import serializers
from two_disgits_prize.models import Two_lower, Two_upper
# from django.utils.module_loading import import_string

# Instalment = import_string('instalment.models.Instalment')


# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['date', 'created_on']


class Two_lowerSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Two_lower
        fields = '__all__'

class Two_upperSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Two_upper
        fields = '__all__'