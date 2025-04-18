from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view
from core.models import User
from core.serializers import UserSerializer

@extend_schema_view(
    list=extend_schema(tags=["Usuários"]),
    create=extend_schema(tags=["Usuários"]),
    retrieve=extend_schema(tags=["Usuários"]),
    update=extend_schema(tags=["Usuários"]),
    partial_update=extend_schema(tags=["Usuários"]),
    destroy=extend_schema(tags=["Usuários"]),
    me=extend_schema(tags=["Usuários"], description="Retorna o usuário autenticado")
)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Return the current authenticated user"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
