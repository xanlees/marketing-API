
from rest_framework import serializers
from predictlose_three.models import Predictlose_three
# from django.utils.module_loading import import_string
# from django.conf import settings

# Instalment = import_string('instalment.models.Instalment')


# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['id', 'date', 'created_on']


class Predictlose_threeSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Predictlose_three
        fields =  '__all__'
