from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    preparo = models.TextField()
    porcao = models.PositiveIntegerField()
    tempoPreparo = models.CharField(max_length=100)
    publicacao = models.DateTimeField(auto_now=True)
    infoAdicional = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nome

    class Meta:
         verbose_name_plural = 'Receitas'
