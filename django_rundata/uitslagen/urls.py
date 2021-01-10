from django.urls import path
from . import views

urlpatterns = [
    path('example', views.home, name = 'uitslagen-home'),
    path('analyse', views.analysed_uitslagen, name = 'anayled-uitslagen'),
    path('multipleregressie', views.analysed_uitslagen_multiple_regressie, name='aumr')
]