from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Machine(models.Model):
    codigo = models.CharField(max_length=200)
    reg_date = models.DateTimeField("date registered")
    status = models.BooleanField(default=False)

class ClientMachine(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()