from django.core.exceptions import ValidationError
from django.db import models


def validar_email_gmail(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('O e-mail deve terminar com @gmail.com')


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, validators=[validar_email_gmail])
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
