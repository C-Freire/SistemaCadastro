from sys import maxsize
from django.db import models
from django.forms import CharField, IntegerField

class Ativo(models.Model):
    
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    fornecedor = models.CharField(max_length=300)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    qtd = models.IntegerField()
    plaqueta = models.IntegerField()
    
    def __str__(self):
        return self.nome
    
    class Meta():
        ordering = ['nome']
        
class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    ativos = models.ManyToManyField(Ativo, through='CategoriaAtivos')
    def __str__(self):
        return self.nome
    
    
    class Meta():
        ordering = ['nome']
        
        
class CategoriaAtivos(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.categoria.nome + " - " + self.ativo.nome
    
    
    class Meta():
        ordering = ['categoria', 'ativo']