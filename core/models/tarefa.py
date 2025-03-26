from django.db import models
from django.core.exceptions import ValidationError
from .user import User
from .categoria import Categoria

class Tarefa(models.Model):
    class TaskStatus(models.TextChoices):
        PENDENTE = "pendente"
        EM_ANDAMENTO = "em_andamento"
        CONCLUIDA = "concluida"
        ATRASADA = "atrasada"
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="tarefas")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_limite = models.DateTimeField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tarefas")
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDENTE,
    )

    def __str__(self):
        return f"{self.titulo} | ({', '.join([categoria.nome for categoria in self.categoria.all()])})"