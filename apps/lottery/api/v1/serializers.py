from django.conf import settings
from django.utils.module_loading import import_string
from parler_rest.serializers import TranslatableModelSerializer
from lottery.models import Lottery
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

TranslatedSerializerMixin = import_string(settings.TRANSLATE_MIXIN)
DRFTranslatedFieldsField = import_string(settings.TRANSLATE_FIELD)


class LotterySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = DRFTranslatedFieldsField(shared_model=Lottery)
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    image = HyperlinkedSorlImageField('1024')

    class Meta:
        model = Lottery
        fields = '__all__'
