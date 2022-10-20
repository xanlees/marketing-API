
from rest_framework import serializers
from two_disgits_prize.models import Two_disgits_prize
from django.utils.module_loading import import_string


# Instalment = import_string('instalment.models.Instalment')


# # class InstalmentSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Instalment
# #         fields = ('date')


class Two_disgits_prizeSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Two_disgits_prize
        fields = '__all__'
