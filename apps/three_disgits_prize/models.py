

from django.db import models
from lottery.models import Lottery


class Threelower(models.Model):
    number = models.IntegerField()
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='threelower')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Three_lower")
        verbose_name_plural = ("Three_lower")

    def __str__(self):
        return str(self.number)

from django.db import models
from lottery.models import Lottery


class Threeupper(models.Model):
    number = models.IntegerField()
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='Threeupper')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Three_upper")
        verbose_name_plural = ("Three_upper")

    def __str__(self):
        return str(self.number)