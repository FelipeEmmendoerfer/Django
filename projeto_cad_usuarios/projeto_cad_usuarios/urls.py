
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de identificação da rota
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('listagem_usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
]
