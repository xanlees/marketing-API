
from django.contrib.auth.models import User
from django.db import models


class Commission(models.Model):
    commission = models.FloatField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commission')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = ("Commission")
        verbose_name_plural = ("Commissions")
    
