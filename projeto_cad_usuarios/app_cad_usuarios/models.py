from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
