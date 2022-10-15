
from django.db import models
from lottery.models import Lottery


class Two_lower(models.Model):
    number = models.IntegerField()
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='two_lower')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Two_lower")
        verbose_name_plural = ("Two_lower")

    def __str__(self):
        return str(self.number)


class Two_upper(models.Model):
    number = models.IntegerField()
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='two_upper')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Two_upper")
        verbose_name_plural = ("Two_upper")

    def __str__(self):
        return str(self.number)
