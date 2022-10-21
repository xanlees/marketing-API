
from rest_framework import serializers
from predictlose_two.models import Predictlose_two
from django.utils.module_loading import import_string


# Instalment = import_string('instalment.models.Instalment')


# # class InstalmentSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Instalment
# #         fields = ('date')


class Predictlose_twoSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Predictlose_two
        fields = '__all__'
