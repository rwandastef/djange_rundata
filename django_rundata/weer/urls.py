from django.urls import path
from . import views

urlpatterns = [
    path('', views.weer_analyse, name = 'weer-analyse'),
    path('/list', views.weer_list, name = 'list')
]