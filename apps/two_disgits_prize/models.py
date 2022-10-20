
from django.db import models
from instalment.models import Instalment
from lottery.models import Lottery


class Two_disgits_prize(models.Model):
    number = models.CharField(max_length=2)
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='two_disgits_prize')
    
    # instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='two_disgits_prize')

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Two_disgits_prize")
        verbose_name_plural = ("Two_disgits_prizes")

    def __str__(self):
        return self.number

