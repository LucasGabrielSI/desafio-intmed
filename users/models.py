from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='E-mail', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
