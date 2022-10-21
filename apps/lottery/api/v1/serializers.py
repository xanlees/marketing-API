# from lottery_time.models import Lottery_time
from asyncore import read
from django.conf import settings
from django.utils.module_loading import import_string
from parler_rest.serializers import TranslatableModelSerializer
from lottery.models import Lottery
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from rest_framework import serializers

TranslatedSerializerMixin = import_string(settings.TRANSLATE_MIXIN)
DRFTranslatedFieldsField = import_string(settings.TRANSLATE_FIELD)
Lottery_day = import_string(settings.LOTTERY_DAY_MODEL)
Lottery_time = import_string(settings.LOTTERY_TIME_MODEL)


class Lottery_Lottery_time_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_time
        fields = ['open_date', 'closing_date']


class Lottery_Lottery_daySerializer(serializers.ModelSerializer):
    lottery_time = Lottery_Lottery_time_Serializer(many=True, read_only=True)

    class Meta:
        model = Lottery_day
        # fields = ['days']
        fields = ['days', 'lottery_time']


class LotterySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = DRFTranslatedFieldsField(shared_model=Lottery)
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True

    )
    image = HyperlinkedSorlImageField('1024')
    lottery_day = Lottery_Lottery_daySerializer(many=True, read_only=True)

    class Meta:
        model = Lottery
        fields = ['translations', 'thumbnail', 'image',
                  'code', 'lottery_day']
