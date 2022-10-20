
from django.db import models
from instalment.models import Instalment
from lottery.models import Lottery


class Khus_kick(models.Model):
    name = models.CharField(max_length=15)
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='khus_kick')
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='khus_kick')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Khus_kick")
        verbose_name_plural = ("Khus_kick")

    def __str__(self):
        return self.name

