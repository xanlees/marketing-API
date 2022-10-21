
from enum import auto
from django.contrib.auth.models import User
from django.db import models
import datetime
from lottery_day.models import Lottery_day
from lottery_time.models import Lottery_time



class Instalment(models.Model):
    date = models.DateField(auto_now_add=True)
    lottery_day = models.ForeignKey(
        Lottery_day, on_delete=models.CASCADE, related_name='instalment')
    lottery_time = models.ForeignKey(Lottery_time, on_delete=models.CASCADE, related_name='instalment')

    class Meta:

        verbose_name = ("Instalment")
        verbose_name_plural = ("Instalments")

    def __str__(self):
       return str (self.date)

