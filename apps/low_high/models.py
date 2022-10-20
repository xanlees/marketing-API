
from django.db import models
from instalment.models import Instalment
from lottery.models import Lottery


class Low_high(models.Model):
    name = models.CharField(max_length=15)
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='low_high')
    # instalment = models.ForeignKey(Instalment
    #     , on_delete=models.CASCADE, related_name='low_high')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Low_high")
        verbose_name_plural = ("Low_high")

    def __str__(self):
        return self.name
    





