from django.db import models

class post(models.Model):
    titulo      = models.CharField(max_length=200)
    corpo       = models.TextField()
    created     = models.DateField
    published   = models.BooleanField(default=False)