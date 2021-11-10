# 📚 Djanblog
Djanblog é um app django para gerenciar um blog simples.

Funcionalidades
- Gerenciar postagens (criar, editar, deletar)
- Gerenciar tags
- Postagens em rascunho (draft)

Djanblog usa PostgreSQL e pode ser deployado em plataformas de núvem como Heroku ou Aws.

## Instalação do Django e do app
### Instalar o Django
- Instalar Python
- Criar pasta do projeto
- Criar ambiente virtual: python -m venv /local/do/venv
- Ativar o ambiente virutal
    - Para Linux/Mac: source activate
    - para Windows 10: Scripts/Activate.ps1 (talvez você precise executar Set-ExecutionPolicy Unrestricted, no poweshell aberto como admin para executar scripts)
- Instalar o Django e demais requisitos: python -m pip install Django
- Criar um novo projeto: django-admin startproject nomedoprojeto
- Rodar no servidor local: python manage runserver
- Criar usuario admin: python manage createsuperuser

### Instalar o app
- Salvar a pasta blog dentro da aplicação Django
- Adicionar 'blog' em INSTALLED_APPS no arquivo settings
- Adicionar `path('blog/', include('blog.urls'))` ao url_patterns no arquivo `urls.py` principal
- Criar e rodar migrations: python manage makemigrations blog / python manage migrate 
- Se o ambiente admin já estiver configurado, é possivel ver os posts e tags para gerenciar

## Endpoints
O djanblog serve conteúdos para consulta como uma API, em formato json.
Os endpoints são:
- blog/posts/all: retorna todos os posts
- blog/post/{slug}: retorna o post identificado pelo slug (único)
- blog/posts/{tag}: retorna todas as postagens com a tag