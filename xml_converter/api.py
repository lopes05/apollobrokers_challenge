from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml_converter.serializers import XMLConverterSerializer

class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer_class = XMLConverterSerializer(data=request.data, context={'request': request, 'view': self})
        serializer_class.is_valid(raise_exception=True)
        return Response(serializer_class.save())
