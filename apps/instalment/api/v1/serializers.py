
from rest_framework import serializers
from instalment.models import Instalment


class InstalmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instalment
        fields = '__all__'

