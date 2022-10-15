from lottery.models import Lottery
from django.db import models


class Lottery_day(models.Model):
    days = models.CharField(max_length=255)
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='lottery_time')


class Meta:
    verbose_name = ("day")
    verbose_name_plural = ("days")
