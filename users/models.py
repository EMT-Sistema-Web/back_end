from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Regular User'),
    )
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username
