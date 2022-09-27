import json

from parler_rest.fields import TranslatedFieldsField


class DRFTranslatedFieldsField(TranslatedFieldsField):
    def to_internal_value(self, data):
        try:
            data = json.loads(data)
        except:
            self.fail('invalid')
        return super().to_internal_value(data)
