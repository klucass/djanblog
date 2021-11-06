# 📚 Djanblog
Djanblog é um app django para gerenciar um blog simples.

Funcionalidades
- Gerenciar postagens (criar, editar, deletar)
- Gerenciar tags
- Postagens em rascunho (draft)

Djanblog usa PostgreSQL e pode ser deployado em plataformas de núvem como Heroku ou Aws.

## Instalação
Instalar o Django
- Instalar Python
- Criar pasta do projeto
- Criar ambiente virtual: python -m venv /local/do/venv
- Ativar o ambiente virutal
    - Para Linux/Mac: source activate
    - para Windows 10: Scripts/Activate.ps1 (talvez você precise executar Set-ExecutionPolicy Unrestricted, no poweshell aberto como admin para executar scripts)
- Instalar o Django e demais requisitos: python -m pip install Django
- Criar um novo projeto: django-admin startproject nomedoprojeto
- Rodar no servidor local: python manage.py runserver