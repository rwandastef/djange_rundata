from django.urls import path
from . import views

urlpatterns = [
    path('example', views.home, name = 'uitslagen-home'),
    path('analyse', views.analysed_uitslagen, name = 'anayled-uitslagen')
]