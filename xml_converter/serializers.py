from rest_framework import serializers
from xml_converter.xml_conversion import InvalidXMLError, XMLConverterToDict

class XMLConverterSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):
        try:
            client = XMLConverterToDict(validated_data["file"])
            result = client.to_dict()
        except InvalidXMLError as e:
            raise serializers.ValidationError({'file': str(e)})
        return result
