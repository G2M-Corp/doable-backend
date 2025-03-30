from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1
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
