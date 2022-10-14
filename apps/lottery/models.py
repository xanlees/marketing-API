from enum import unique
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from sorl.thumbnail import ImageField
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


class Lottery(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=200,
                              db_index=True, unique=True),
    )
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lottery')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Lottery")
        verbose_name_plural = _("Lotteries")

    def __str__(self):
        return self.name


def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)
