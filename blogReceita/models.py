from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    #imagem = models.ImageField(null=True, blank=True, upload_to='imagens')
    ingredientes = models.TextField(null=False, blank=False)
    preparo = models.TextField(null=False, blank=False)
    porcao = models.PositiveIntegerField(null=False, blank=False)
    tempoPreparo = models.CharField(max_length=100, null=False, blank=False)
    publicacao = models.DateTimeField(auto_now=True)
    infoAdicional = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
         verbose_name_plural = 'Receitas'
