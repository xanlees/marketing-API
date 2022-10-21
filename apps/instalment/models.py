
from django.contrib.auth.models import User
from django.db import models
from lottery_time.models import Lottery_time



class Instalment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    # lottery = models.ForeignKey(
    #     Lottery, on_delete=models.CASCADE, related_name='instalment')
    lottery_time = models.ForeignKey(Lottery_time, on_delete=models.CASCADE, related_name='instalment')

    class Meta:
        ordering = ['-created_on']
        verbose_name = ("Instalment")
        verbose_name_plural = ("Instalments")

    def __str__(self):
       return self.created_on

