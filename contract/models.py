from django.db import models

from machine.models import Machine


class ClientMachine(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    
class Contract(models.Model):
    client = models.ForeignKey(ClientMachine, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    type = models.CharField(choices=[('compra', 'Compra'), ('aluguel', 'Aluguel')], max_length=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)  
    valid = models.BooleanField(default=True)