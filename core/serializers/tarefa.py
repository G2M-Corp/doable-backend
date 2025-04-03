from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    DateTimeField,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    SlugRelatedField,
)
from datetime import date
from core.models import Tarefa, Categoria
from core.serializers import CategoriaSerializer

from uploader.models import Image
from uploader.serializers import ImageSerializer

class TarefaSerializer(ModelSerializer):
    usuario = CharField(source="usuario.username", read_only=True)
    categorias = CategoriaSerializer(many=True, read_only=True)
    criado_em = DateTimeField(read_only=True)
    imagem_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(
        required=False,
        read_only=True
    )

    class Meta:
        model = Tarefa
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        categorias_data = self.initial_data.get("categorias")
        tarefa = Tarefa.objects.create(**validated_data)
        for categoria_data in categorias_data:
            categoria, created = Categoria.objects.get_or_create(**categoria_data)
            tarefa.categorias.add(categoria)
        return tarefa


class TarefaCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Tarefa
        fields = "__all__"

    def validate_prazo(self, data_limite):
        if data_limite < date.today():
            raise ValidationError("A data de prazo não pode ser no passado.")
        return data_limite


class TarefaListSerializer(ModelSerializer):
    categoria = CharField(source="categoria.nome", read_only=True)
    status_display = SerializerMethodField()
    imagem = ImageSerializer(required=False)

    def get_status_display(self, instance):
        return instance.get_status_display()

    class Meta:
        model = Tarefa
        fields = "__all__"