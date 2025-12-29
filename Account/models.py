from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Profil Resmi")
    biography = models.CharField(max_length=300, blank=True, null=True, verbose_name='Biyografi')

    def __str__(self):
        return self.username

    @property
    def fullname(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username