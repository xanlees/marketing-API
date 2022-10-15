from unicodedata import name
from django.db import models
from lottery.models import Lottery
from sorl.thumbnail import delete
from django_cleanup.signals import cleanup_pre_delete
# Create your models here.


class Instalment(models.Model):
    date = models.DateField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='instalment')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("Instalment")
    verbose_name_plural = ("Instalment")

    
