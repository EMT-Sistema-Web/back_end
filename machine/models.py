from django.db import models

class Machine(models.Model):
    code = models.CharField(max_length=200)
    reg_date = models.DateTimeField("date registered")
    status = models.BooleanField(default=False)
