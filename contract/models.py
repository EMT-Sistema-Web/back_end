from django.db import models

class Contract(models.Model):
    client = models.ForeignKey(ClientMachine, on_delete=models.CASCADE)
    machine = models.ForeignKey(Maqhine, on_delete=models.CASCADE)
    type = models.CharField(choices=[('compra', 'Compra'), ('aluguel', 'Aluguel')], max_length=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)  
    valid = models.BooleanField(default=True)