
from rest_framework import serializers
from khus_kick.models import Khus_kick

class Khus_kickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Khus_kick
        fields = '__all__'

