
from django.db import models
from enum import Enum


class Type(Enum):
    Three_digists = "3 ໂຕ "
    Two_digists = "2 ໂຕ"
    Low_High = "ຕໍ່າ/ສູງ"
    Evennumber_Primenumber = "ຄູ່/ຄີກ"
    Wings = "ວິງ"


class Lottery_type(models.Model):

    type = models.CharField(choices=[(tag.name, tag.value)
                                     for tag in Type], max_length=50, default='Three_digists', blank=True)
    mutiple = models.FloatField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_on']
        verbose_name = ("Lottery_type")
        verbose_name_plural = ("Lottery_types")

    def __str__(self):
        return self.type
