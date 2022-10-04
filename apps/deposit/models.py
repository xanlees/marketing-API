from django.contrib.auth.models import User
from django.db import models


class Deposit(models.Model):
    deposit_amount = models.BigIntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='deposit')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = ("Deposit")
        verbose_name_plural = ("Deposits")

    def __str__(self):
        return self.deposit_amount


