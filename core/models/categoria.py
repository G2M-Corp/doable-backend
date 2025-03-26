from django.db import models
from .user import User

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="categorias")

    def __str__(self):
        return f"{self.nome}"