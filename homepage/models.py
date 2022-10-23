from django.db import models
from django.utils import timezone

class Data(models.Model):
    provinsi = models.CharField(max_length=60)
    positive = models.BigIntegerField(default=0)
    death = models.BigIntegerField(default=0)
    recovered = models.BigIntegerField(default=0)
    date = models.DateField(default=timezone.now)