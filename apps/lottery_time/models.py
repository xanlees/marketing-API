from django.db import models
from lottery.models import Lottery
# from django.conf import settings
# from django.utils.module_loading import import_string

# Lottery = import_string(settings.LOTTERY_MODEL)
# Lottery = import_string('lottery.models.Lottery')

class Lottery_time(models.Model):
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='lottery_time')
    open_date = models.DateTimeField()
    closing_date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = ("Lottery_time")
        verbose_name_plural = ("Lottery_time")



