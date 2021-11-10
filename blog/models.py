from django.db import models
from tinymce.models import HTMLField
from datetime import datetime


class Tag(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo      = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=240, null=True, unique=True)
    corpo       = HTMLField()
    rascunho    = models.BooleanField(default=True)
    tags        = models.ManyToManyField(Tag)
    data        = models.DateField(default=datetime.now)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo