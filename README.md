# Projeto Cadastro de Usuários

Este projeto é uma aplicação Django simples para cadastro e login de usuários.

## Funcionalidades

- Tela de login
   * Compara a existência do usuário e da senha com as salvas no banco de dados para liberar acesso a "listagem_usuarios"
- Tela de cadastro
* Salva os dados do usuário no banco de dados
- Listagem de usuários
* Exibe o id (enumera por ordem de criação), nome, senha e email. 
- Mostrar/ocultar senha
  * Opção adicional apenas para enfeitar
- Adicionais
  * O programa possui diversas mensagens de erro e manipulação de exceções para casos onde o usuário tente deixar campos em branco ou não adicionar parâmetros básicos, há uma pagina para redefinição de senha superficial sem proposito ainda. 

## Requisitos

- Python 3.10+
- Django 6.0.7

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python manage.py runserver
```

A aplicação ficará disponível em http://127.0.0.1:8000/
