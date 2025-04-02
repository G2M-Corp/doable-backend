from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import User


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = "__all__"
        depth = 1
        read_only_fields = ['is_staff', 'is_superuser']
        extra_kwargs = {
            'imagem': {'required': False, 'allow_null': True}
        }
        
    imagem_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        allow_null=True,
        write_only=True,
    )
    imagem = ImageSerializer(
        required=False,
        read_only=True,
        allow_null=True
    )
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        
        if password:
            user.set_password(password)
            user.save()
            
        return user
