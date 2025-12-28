from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    biography = models.CharField(max_length=300, blank=True, null=True, verbose_name='Açıklama')

    def __str__(self):
        return self.username