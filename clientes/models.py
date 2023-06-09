from django.db import models

class Clientes(models.Model):
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    email = models.EmailField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

    def __str__(self):
        return self.nome
    
class Meta:
        verbose_name_plural = 'Cliente'