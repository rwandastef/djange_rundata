from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from pymongo import MongoClient
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from uitslagen.helpers.gender import selectMen, selectWomen
from uitslagen.serializer import UitslagSerializer, AnalysedUitslagenSerializer
from uitslagen.models import Uitslag, AnalysedUitslagen
import logging
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from calendar import isleap
from scipy import stats
import json
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression, ElasticNet, Lasso, Ridge
from sklearn import metrics




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
def analysed_uitslagen(request):
    logger.debug('enter post')
    client = MongoClient()
    db = client.runners_db
    if request.method == 'GET':
        collection = db.uitslagen
        data = pd.DataFrame(list(collection.find()))
        mean_runtime = data["time in seconds"].mean()/60
        mean_runtime_men = selectMen(data)["time in seconds"].mean()/60
        mean_runtime_women = selectWomen(data)["time in seconds"].mean()/60
        endTime = data.iloc[:, 5].values
        dateNumber = data.iloc[:, 8].values
        coef, intercept, p_value, accuracie = lr_2d(data, dateNumber, endTime)
        analysedUitslagen = AnalysedUitslagen(mean_runtime, coef, intercept, p_value, accuracie,
                                              mean_runtime_men, mean_runtime_women)
        serializer = AnalysedUitslagenSerializer(analysedUitslagen)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def analysed_uitslagen_multiple_regressie(request):
    logger.debug('enter method')
    client = MongoClient()
    db = client.runners_db
    if request.method == 'GET':
        collection = db.uitslagen
        data = pd.DataFrame(list(collection.find()))
        return JsonResponse({'result': 'still to be implemented'}, status=status.HTTP_200_OK, safe=False)


def lr_2d(df, data, target):
    """" returns a tuple of coe_ef and intercept and R2 of 2d dataset lineair regression"""

    X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=11)
    lr = LinearRegression()
    lr.fit(X=X_train.reshape(-1,1), y=y_train)
    predicted = lr.predict(X_test.reshape(-1,1))
    expected = y_test
    accuracie = metrics.r2_score(expected, predicted)
    # get p-value
    p_value = stats.linregress(x = df['dateNumber'], y = df['time in seconds']).pvalue
    return lr.coef_[0], lr.intercept_, p_value, accuracie
    
def lr_ontarget_endTime(df):
    """" linear regression gender, temperatere, datenumber, regioCode on
    target: time in seconds"""
    #df = df.sample(frac=0.5, replace=True, random_state=1)
    del df['date']
    del df['provincie']
    del df['cat']
    del df['Column1']
    target = df['time in seconds'].values
    del df['time in seconds']

    # split in train set and test set
    X_train, X_test, y_train, y_test = train_test_split(df, target, random_state=11)
    # start multi dimensional regression
    lr = LinearRegression()
    lr.fit(X=X_train, y=y_train)
    print(lr.intercept_)
    for i, name in enumerate(df.columns[0:4]):
        print(f'{name:>10}: {lr.coef_[i]}')

    # testing result of training
    predicted = lr.predict((X_test))
    expected = y_test
    comparedDf = pd.DataFrame()
    comparedDf['Expected'] = pd.Series(expected)
    comparedDf['Predicted'] = pd.Series(predicted)




    # How good is the model
    # R2 between 0 and 1 (1 is the perfect model)
    accuracie = metrics.r2_score(expected, predicted)
    print(accuracie)

    # apply different estimators
    estimators = {
        'LR': lr,
        'ElasticNet': ElasticNet(),
        'Lasso': Lasso(),
        'Ridge': Ridge()
    }
    logger.warning(df.columns)
    # cros_val_score is de uitkomst van 1 van de Kfold set
    # in ons geval 9 sets, gebruikt voor trainen, van elk de r2 score en daarvan berekenen we gemiddelde
    for estimator_name, estimator_object in estimators.items():
        kfold = KFold(n_splits=10, random_state=11, shuffle=True)
        scores = cross_val_score(estimator_object, X=df, y= target, cv= kfold, scoring='r2')
        print(f'{estimator_name}: '
              + f'mean of r2 scores = {scores.mean():3f}')

    # return lr


