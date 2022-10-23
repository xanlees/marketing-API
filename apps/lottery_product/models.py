
from tkinter import CASCADE
from django.db import models
from lottery_type.models import Lottery_type
from instalment.models import Instalment
from enum import Enum


class Status(Enum):
    Top = "ບົນ"
    Bottom = "ລ່າງ"


class Lottery_product(models.Model):
    lottery_name = models.CharField(max_length=10)
    status = models.CharField(choices=[(tag.name, tag.value)
                                       for tag in Status], max_length=50, default='Top', blank=True)
    limitcost = models.IntegerField()
    lottery_type = models.ForeignKey(
        Lottery_type, on_delete=models.CASCADE, related_name='lottery_product')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Lottery_product")
        verbose_name_plural = ("Lottery_products")

    def __str__(self):
        return self.lottery_name
