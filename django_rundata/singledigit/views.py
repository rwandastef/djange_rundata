from django.shortcuts import render
import logging
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
import pymongo as pm
from pymongo import MongoClient
import pandas as pd


from singledigit.kaggle_code import verwerkImage

pd.options.mode.chained_assignment = None  # default='warn'
from calendar import isleap
from scipy import stats
import json

# This retrieves a Python logging instance (or creates it)
from weer.models import Weer, WeerAnalyse
from weer.serializer import WeerSerializer, WeerAnalyseSerializer
import datetime as dt

logger = logging.getLogger(__name__)


# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def test(request):
    logger.debug('enter post')
    if request.method == 'GET':
        return JsonResponse({'response': 'test digit analyser'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def upload_digit(request):
    logger.debug('enter post')
    if request.method == 'POST':
        iets = request.FILES
        logger.warning('yes hij komt tot hier')
        verwerkImage(iets)
        return JsonResponse({'response': 'hello, thank for your upload'}, status=status.HTTP_201_CREATED, safe=False)