from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField
from parler.models import TranslatableModel, TranslatedFields
from sorl.thumbnail import ImageField
from enumchoicefield import ChoiceEnum, EnumChoiceField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


class Audience(ChoiceEnum):
    Public = "Public"
    Preview = "Preview"
    Archive = "Archive"


class Product(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("title"), max_length=200, db_index=True),
        description=models.TextField(_("Description"), blank=True),
    )
    slug = models.SlugField(max_length=100, unique=True,
                            db_index=True, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='LAK')
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product')
    audience = EnumChoiceField(Audience, default=Audience.Public)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title



def sorl_delete(**kwargs):
    delete(kwargs['file'])

cleanup_pre_delete.connect(sorl_delete)