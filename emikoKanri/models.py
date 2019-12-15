from django.conf import settings
from django.db import models
from django.utils import timezone


class NurseRecord(models.Model):
    nurse_day = models.DateField()
    urine_time = models.CharField(max_length=5, null=True)
    urine_volume = models.PositiveIntegerField(null=True)
    memo = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.memo

 