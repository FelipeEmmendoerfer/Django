from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'Login/login.html')


def register(request):
    return render(request, 'Login/register.html')


def forgot_password(request):
    return render(request, 'Login/forgot_password.html')