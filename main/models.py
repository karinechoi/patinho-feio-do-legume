# main/models.py
from django.db import models
from produtoWebserver.settings import DEFAULT_FILE_STORAGE
from django.contrib.auth.models import AbstractUser

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    foto = models.ImageField(upload_to= DEFAULT_FILE_STORAGE)  # Requer configuração do servidor de mídia
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    id_agricultor = models.IntegerField()
    classificacao = models.DecimalField(max_digits=3, decimal_places=1)
    tipo_produto = models.CharField(max_length=100)
    tipo_medida = models.CharField(max_length=50)

    class Meta:
        app_label = 'produtoWebserver'
    def __str__(self):
        return self.nome

class User(AbstractUser):
    USUARIO_CHOICES = [
        ('AGRICULTOR', 'Agricultor'),
        ('CONSUMIDOR', 'Consumidor'),
    ]

    celular = models.CharField(max_length=15, blank=True)
    tipo_usuario = models.CharField(max_length=10, choices=USUARIO_CHOICES, null=True)

    class Meta:
        app_label = 'main'
