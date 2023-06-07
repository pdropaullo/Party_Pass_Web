from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Comandas(models.Model):
    cliente = models.ForeignKey('clientes.Clientes', on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.saldo

    class Meta:
        verbose_name_plural = 'Comandas'


class Clientes(models.Model):    
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Comandas'