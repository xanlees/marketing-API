
from rest_framework import serializers
from low_high.models import Low_high

class Low_highSerializer(serializers.ModelSerializer):

    class Meta:
        model = Low_high
        fields = '__all__'
