from enum import unique
from django.db import models
from lottery_day.models import Lottery_day

class Lottery_time(models.Model):
    lottery_day = models.ForeignKey(
        Lottery_day, on_delete=models.CASCADE, related_name='lottery_time')
    open_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    class Meta:
        verbose_name = ("Lottery_time")
        verbose_name_plural = ("Lottery_time")
