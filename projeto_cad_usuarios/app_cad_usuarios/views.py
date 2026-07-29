from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario


# Create your views here.
def login(request):
    if request.method == 'POST':
        nome_digitado = (request.POST.get('username') or '').strip()
        senha_digitada = (request.POST.get('password') or '').strip()

        for usuario in Usuario.objects.all():
            nome_cadastrado = (usuario.nome or '').strip()
            senha_cadastrada = (usuario.senha or '').strip()

            if nome_cadastrado == nome_digitado and senha_cadastrada == senha_digitada:
                return redirect('listagem_usuarios')

        messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'Login/login.html')


def register(request):
    if request.method == 'POST':
        nome = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip()
        senha = (request.POST.get('password1') or '').strip()
        confirmar_senha = (request.POST.get('password2') or '').strip()

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'Login/register.html')

        Usuario.objects.create(nome=nome, email=email, senha=senha)
        messages.success(request, 'Usuário criado com sucesso!')
        return render(request, 'Login/register.html')

    return render(request, 'Login/register.html')


def forgot_password(request):
    return render(request, 'Login/forgot_password.html')


# salvar dados do usuário no banco de dados
def listagem_usuarios(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'Login/listagem_usuarios.html', usuarios)

