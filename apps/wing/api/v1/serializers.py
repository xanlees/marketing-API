
from rest_framework import serializers
from wing.models import Wing
# from django.utils.module_loading import import_string

# Instalment = import_string('instalment.models.Instalment')


# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['date', 'created_on']


class WingSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Wing
        fields = '__all__'
