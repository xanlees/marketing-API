

from django.db import models
from instalment.models import Instalment


class Predictlose_three(models.Model):
    number = models.CharField(max_length=3)
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='predictlose_three')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Predictlose_three")
        verbose_name_plural = ("Predictlose_threes")

    def __str__(self):
        return self.number
