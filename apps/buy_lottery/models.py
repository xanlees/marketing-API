from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User


class Buy_Lottery(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='number')
    number = models.IntegerField()
    amount_buy_top = models.IntegerField(blank=True)
    amount_buy_bottom = models.IntegerField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_on']
    verbose_name = ("number")
    verbose_name_plural = ("numbers")
