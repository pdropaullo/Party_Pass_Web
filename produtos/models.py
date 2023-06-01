from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=15)
    descricao = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        verbose_name_plural = 'Produtos'