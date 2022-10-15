
from django.db import models
from lottery.models import Lottery


class Low_lower(models.Model):
    name = models.CharField(max_length=15)
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='low_lower')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Low_lower")
        verbose_name_plural = ("Low_lower")

    def __str__(self):
        return self.name
    

from django.db import models
from lottery.models import Lottery

class High_upper(models.Model):
    name = models.CharField(max_length=15)
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='high_upper')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("High_upper")
        verbose_name_plural = ("High_upper")

    def __str__(self):
        return self.name

from django.db import models
from lottery.models import Lottery

class Low_upper(models.Model):
    name = models.CharField(max_length=15)
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='low_upper')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("Low_upper")
        verbose_name_plural = ("Low_upper")

    def __str__(self):
        return self.name
    
from django.db import models
from lottery.models import Lottery

class High_lower(models.Model):
    name = models.CharField(max_length=15)
    sales = models.FloatField()
    win = models.FloatField()
    lottery = models.ForeignKey(
        Lottery, on_delete=models.CASCADE, related_name='high_lower')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = ("High_lower")
        verbose_name_plural = ("High_lower")

    def __str__(self):
        return self.name