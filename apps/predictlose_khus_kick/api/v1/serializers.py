
from rest_framework import serializers
from predictlose_khus_kick.models import Predictlose_khus_kick

class Khus_kickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Predictlose_khus_kick
        fields = '__all__'

