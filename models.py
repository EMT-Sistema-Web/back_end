# machbase/models.py
from django.db import models
from base import MachbaseModel
from manage import MachbaseManager

class SensorData(MachbaseModel):
    timestamp = models.DateTimeField(primary_key=True)
    device_id = models.CharField(max_length=50)
    value = models.FloatField()
    
    objects = MachbaseManager(table_name='SENSOR_DATA')

    class Meta:
        db_table = 'SENSOR_DATA'
        managed = False