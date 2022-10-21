
from django.db import models
from instalment.models import Instalment



class Predictlose_low_high(models.Model):
    name = models.CharField(max_length=15)
    instalment = models.ForeignKey(Instalment
        , on_delete=models.CASCADE, related_name='predictlose_low_high')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("predictlose_low_high")
        verbose_name_plural = ("predictlose_low_highs")

    def __str__(self):
        return self.name
    





