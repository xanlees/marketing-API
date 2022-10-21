
from django.db import models
from instalment.models import Instalment



class Predictlose_wing(models.Model):
    name = models.CharField(max_length = 13)
    # number_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=1)
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='predictlose_wing')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Predictlose_wing")
        verbose_name_plural = ("Predictlose_wings")

    def __str__(self):
        return self.name
