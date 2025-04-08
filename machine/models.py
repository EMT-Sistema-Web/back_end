from django.db import models

class TemperatureReading(models.Model):
    temperature_raw = models.IntegerField(  # Armazena 36.5°C como 365
        help_text="Numero inteiro"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def temperature(self) -> float:
        #(dividido por 10)
        return self.temperature_raw / 10

    @temperature.setter
    def temperature(self, value: float):
        #(multiplica por 10)
        self.temperature_raw = int(round(value * 10))
        return self.temperature_raw

    
class Temperature(models.Model):
    type = models.CharField(choices=[('tempCoolant', 'tempCoolant'), ('tempKeyer', 'tempKeyer'), ('tempCoil', 'tempCoil')], max_length=20)
    value = TemperatureReading
    
class Machine(models.Model):
    identificador = models.CharField(max_length=200)
    reg_date = models.DateTimeField("date registered")
    pulses_amount = models.IntegerField()
    use_time = models.DateTimeField("date registered")
    status = models.BooleanField(default=False)
    temperatures = models.ManyToManyField(Temperature)
    treatment_amount = models.IntegerField()
    

    
