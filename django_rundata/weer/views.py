from django.shortcuts import render
from rest_framework.decorators import api_view
import logging
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
import pymongo as pm
from pymongo import MongoClient
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from calendar import isleap
from scipy import stats
import json

# This retrieves a Python logging instance (or creates it)
from weer.models import Weer, WeerAnalyse
from weer.serializer import WeerSerializer, WeerAnalyseSerializer
import datetime as dt

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST', 'DELETE'])
def weer_list(request):
    logger.debug('enter post')
    client = MongoClient()
    db = client.runners_db
    if request.method == 'GET':
        collection = db.people
        data = pd.DataFrame(list(collection.find()))
        data = verwerkWeerTable(data)
        lr = stats.linregress(x=data.dayNumber, y=data.temperature)
        return JsonResponse({'slope': lr.slope, 'intercept': lr.intercept,
                             'rvalue': lr.rvalue, 'pvalue': lr.pvalue}, status=status.HTTP_200_OK, safe=False)


def verwerkWeerTable(data):
    """ maakt van KNMI weergegevens tabel een tabel om verder mee te werken voor lineaire regressie"""
    data = data[['YYYYMMDD', 'TX']]
    data.columns = ['dateAndId', 'temperature']
    data.dateAndId = data.dateAndId.astype(str)
    data['temperature'] = data['temperature'].astype(str)
    data['temperature'] = data['temperature'].str.strip()
    data['temperature'] = data['temperature'].replace('', '1')
    data["temperature"] = data["temperature"].astype(str).astype(int)
    data['s'] = data.dateAndId.apply(lambda x: dt.datetime(int(x[0:4]), int(x[4:6]), int(x[6:8])))
    data['s'] = data.s.dt.strftime('%j').astype(int)
    data['dayNumber'] = data.s + data.dateAndId.apply(lambda x: yearAddDays(1951, int(x[0:4])))
    del data['s']
    data.dateAndId = data.dateAndId.astype(int)
    return data
    
def yearAddDays(start = 2007,givenyear=2020):
    """" given an start year it will calculate how many days to add by given year """
    count = 0
    result = 0
    for ly in range(start+1, givenyear):
        if isleap(ly)==True:
            result = result + 366
        if isleap(ly)==False:
            result = result + 365
    return result