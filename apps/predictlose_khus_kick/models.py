
from django.db import models
from instalment.models import Instalment
from lottery.models import Lottery


class Predictlose_khus_kick(models.Model):
    name = models.CharField(max_length=15)
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='predictlose_khus_kick')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Predictlose_khus_kick")
        verbose_name_plural = ("Predictlose_khus_kicks")

    def __str__(self):
        return self.name

