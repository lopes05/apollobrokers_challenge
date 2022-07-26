from django.http import JsonResponse
from django.shortcuts import render
from xml_converter.xml_conversion import XMLConverterToDict, InvalidXMLError

def upload_page(request):
    if request.method == 'POST':
        xml_file = request.FILES.get('file')
        if not xml_file:
            return JsonResponse({'error': 'No file provided'})
        else:
            try:
                xml_converter = XMLConverterToDict(xml_file)
                return JsonResponse(xml_converter.to_dict())
            except InvalidXMLError as e:
                return JsonResponse({'error': str(e)}, status=400)

    return render(request, "upload_page.html")
