from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Comandas(models.Model):
    saldo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.saldo

    class Meta:
        verbose_name_plural = 'Comandas'
