from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from uitslagen.serializer import UitslagSerializer
from uitslagen.models import Uitslag
import logging




# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

uitslagen = [
    {
        'timeinseconds': 2222,
        'temperature': 150,
        'gender': 0,
        'regioCode': 3,
        'label': 'VR10KMSEN',
        'dayNumber': 232
    },
    {
        'timeinseconds': 3022,
        'temperature': 150,
        'gender': 0,
        'regioCode': 3,
        'label': 'VR10KMSEN',
        'dayNumber': 347
    }
]


def home(request):
    context = {
        'uitslagen': uitslagen
    }
    # return render(request, 'uitslagen/uitslagen.html', context)
    return JsonResponse({'example': 'hallo'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def uitslagen_list(request):
    logger.debug('enter post')
    if request.method == 'GET':
        content = Uitslag.objects.all()
        result = UitslagSerializer(content, many=True)
        logger.warning(result.data)
        return JsonResponse({}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        uitslag_data = JSONParser().parse(request)
        uitslag_serializer = UitslagSerializer(data=uitslag_data)
        if uitslag_serializer.is_valid():
            logger.warning(f'show me the money: {uitslag_serializer}')
            uitslag_serializer.save()
            return JsonResponse(uitslag_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(uitslag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


