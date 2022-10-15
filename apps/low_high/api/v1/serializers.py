
from rest_framework import serializers
from low_high.models import Low_lower, Low_upper, High_lower, High_upper

class Low_lowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Low_lower
        fields = '__all__'

class Low_upperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Low_upper
        fields = '__all__'

class High_lowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = High_lower
        fields = '__all__'

class High_upperSerializer(serializers.ModelSerializer):

    class Meta:
        model = High_upper
        fields = '__all__'
