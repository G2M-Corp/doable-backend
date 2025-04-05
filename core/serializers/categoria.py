from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    ValidationError,
)
from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    usuario = CharField(source="usuario.username", read_only=True)

    class Meta:
        model = Categoria
        fields = "__all__"


class CategoriaCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Categoria
        fields = ("usuario", "nome")

    def validate_nome(self, nome):
        if len(nome.strip()) < 3:
            raise ValidationError("O nome da categoria deve ter pelo menos 3 caracteres.")
        return nome


class CategoriaListSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
