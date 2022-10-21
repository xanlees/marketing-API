
from rest_framework import serializers
from predictlose_wing.models import Predictlose_wing
# from django.utils.module_loading import import_string

# Instalment = import_string('instalment.models.Instalment')


# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['date', 'created_on']


class Predictlose_wingSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Predictlose_wing
        fields = '__all__'
