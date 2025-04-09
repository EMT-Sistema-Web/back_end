from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Dev Admin'),
        (2, 'Magvia Admin'),
        (3, 'Regular User'),
        (4, 'Patient User'),
        
    )
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username
