from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from pymongo import MongoClient
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from uitslagen.serializer import UitslagSerializer, AnalysedUitslagenSerializer
from uitslagen.models import Uitslag, AnalysedUitslagen
import logging
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from calendar import isleap
from scipy import stats
import json




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
    client = MongoClient()
    db = client.runners_db
    if request.method == 'GET':
        collection = db.uitslagen
        data = pd.DataFrame(list(collection.find()))
        mean_runtime = data["time in seconds"].mean()/60
        analysedUitslagen = AnalysedUitslagen(mean_runtime)
        serializer = AnalysedUitslagenSerializer(analysedUitslagen)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    


