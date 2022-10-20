
from django.db import models
from instalment.models import Instalment
from lottery.models import Lottery



class Wing(models.Model):
    number = models.CharField(max_length=1)
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='Wing')
    instalment = models.ForeignKey(Instalment, on_delete=models.CASCADE, related_name='Wing')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Wing_upper")
        verbose_name_plural = ("Wing_uppers")

    def __str__(self):
        return self.number
