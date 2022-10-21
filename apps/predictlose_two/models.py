
from django.db import models
from instalment.models import Instalment



class Predictlose_two(models.Model):
    number = models.CharField(max_length=2)
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='predictlose_two')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Predictlose_two")
        verbose_name_plural = ("Predictlose_twos")

    def __str__(self):
        return self.number

