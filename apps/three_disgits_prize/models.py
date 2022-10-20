

from django.db import models
from lottery.models import Lottery


class Three_disgits_prize(models.Model):
    number = models.CharField(max_length=3)
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='three_disgits_prize')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Three_disgits_prize")
        verbose_name_plural = ("Three_disgits_prizes")

    def __str__(self):
        return self.number
