
from rest_framework import serializers
from predictlose_low_high.models import Predictlose_low_high

class Predictlose_low_highSerializer(serializers.ModelSerializer):

    class Meta:
        model = Predictlose_low_high
        fields = '__all__'
