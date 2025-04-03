import stat
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models.aggregates import Sum
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome", "descricao"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser or usuario.groups.filter(name="admin"):
            return Categoria.objects.all()
        else:
            return Categoria.objects.filter(usuario=usuario)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=["get"])
    def total_by_category(self, request):
        usuario = request.user
        if usuario.is_superuser or usuario.groups.filter(name="admin").exists():
            categorias = Categoria.objects.all()
        else:
            categorias = Categoria.objects.filter(usuario=usuario)

        total = categorias.annotate(total_tarefas=Count("tarefas")).values("nome", "total_tarefas")
        return Response(total, status=status.HTTP_200_OK)