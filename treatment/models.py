from django.db import models
from machine.models import Machine


# Create your models here.
class Treatment(models.Model):
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField("date registered")
    end_date = models.DateTimeField("date registered")
    pulses_amount = models.IntegerField()
    sequence_amount = models.IntegerField()
    use_time = models.DateTimeField("date registered")
    status = models.BooleanField(default=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)