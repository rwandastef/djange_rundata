from django.urls import path
from . import views

urlpatterns = [
    path('', views.weer_list, name = 'weer-list')
]