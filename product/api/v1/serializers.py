from django.conf import settings
from django.utils.module_loading import import_string
from parler_rest.serializers import TranslatableModelSerializer
from product.models import Product
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

ConvertSerializerMixin = import_string(settings.CURRENCY_MIXIN)
TranslatedSerializerMixin = import_string(settings.TRANSLATE_MIXIN)
DRFTranslatedFieldsField = import_string(settings.TRANSLATE_FIELD)


class ProductSerializer(ConvertSerializerMixin, TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = DRFTranslatedFieldsField(shared_model=Product)
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True
    )
    image = HyperlinkedSorlImageField('1024')

    class Meta:
        model = Product
        fields = '__all__'
