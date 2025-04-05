from rest_framework import mixins, parsers, viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from uploader.models import Document, Image
from uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer


@extend_schema_view(
    list=extend_schema(tags=["Upload"]),
    create=extend_schema(tags=["Upload"]),
)
class CreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all() #  pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(CreateViewSet):
    queryset = Image.objects.all() #  pylint: disable=no-member
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
