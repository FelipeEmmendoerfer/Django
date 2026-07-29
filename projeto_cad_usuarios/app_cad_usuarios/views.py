from django.shortcuts import render
from .models import Usuario
# Create your views here.
def login(request):
    return render(request, 'Login/login.html')


def register(request):
    return render(request, 'Login/register.html')


def forgot_password(request):
    return render(request, 'Login/forgot_password.html')
#salvar dados do usuário no banco de dados
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('Usuário')
    novo_usuario.senha = request.POST.get('Senha')
    novo_usuario.email = request.POST.get('Email')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'Login/listagem_usuarios.html', usuarios)

