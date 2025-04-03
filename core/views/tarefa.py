from httpx import request
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models.aggregates import Sum
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from core.models import Tarefa
from core.serializers import TarefaSerializer
from core.serializers import TarefaCreateUpdateSerializer


class TarefaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Tarefa.objects.all()
        if usuario.groups.filter(name="admin"):
            return Tarefa.objects.all()
        return Tarefa.objects.filter(usuario=usuario)

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["status", "data_limite", "categoria"]
    search_fields = ["titulo", "descricao"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return TarefaCreateUpdateSerializer
        return TarefaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @extend_schema(request=None)
    @action(detail=False, methods=["post"])
    def update_overdue_tasks(self, request):
        tarefas_atrasadas = Tarefa.objects.filter(
            prazo__lt=date.today(), status__in=[Tarefa.TaskStatus.PENDENTE, Tarefa.TaskStatus.EM_ANDAMENTO]
        )
        tarefas_atrasadas.update(status=Tarefa.TaskStatus.ATRASADA)
        return Response({"status": "Tarefas atrasadas atualizadas com sucesso."}, status=status.HTTP_200_OK)

    @extend_schema(request=None)
    @action(detail=False, methods=["post"])
    def complete_all_tasks(self, request):
        tarefas = Tarefa.objects.filter(status=Tarefa.TaskStatus.EM_ANDAMENTO)
        tarefas.update(status=Tarefa.TaskStatus.CONCLUIDA)
        return Response({"status": "Todas as tarefas em andamento foram concluídas."}, status=status.HTTP_200_OK)