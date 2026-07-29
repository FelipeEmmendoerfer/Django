from django.test import TestCase
from django.urls import reverse

from .models import Usuario


class LoginTests(TestCase):
    def test_login_invalido_nao_redireciona(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'usuario_inexistente', 'password': 'senha_errada'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Usuário ou senha inválidos.')

    def test_login_valido_redireciona_para_listagem(self):
        Usuario.objects.create(nome='admin', senha='123456', email='admin@gmail.com')

        response = self.client.post(
            reverse('login'),
            {'username': 'admin', 'password': '123456'}
        )

        self.assertRedirects(response, reverse('listagem_usuarios'))

    def test_login_aceita_nome_com_espacos_extras(self):
        Usuario.objects.create(nome='felipe ', senha='cauan123', email='felipe@gmail.com')

        response = self.client.post(
            reverse('login'),
            {'username': 'felipe', 'password': 'cauan123'}
        )

        self.assertRedirects(response, reverse('listagem_usuarios'))
