
from rest_framework import serializers
from three_disgits_prize.models import Three_disgits_prize
# from django.utils.module_loading import import_string
# from django.conf import settings

# Instalment = import_string('instalment.models.Instalment')


# class InstalmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instalment
#         fields = ['id', 'date', 'created_on']


class Three_disgits_prizeSerializer(serializers.ModelSerializer):
    # instalment = InstalmentSerializer(many=True, read_only=True)

    class Meta:
        model = Three_disgits_prize
        fields =  '__all__'
