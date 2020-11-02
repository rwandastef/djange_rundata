from django.urls import path
from . import views

urlpatterns = [
    path('example', views.home, name = 'uitslagen-home'),
    path('', views.uitslagen_list, name = 'uitslagen-list')
]