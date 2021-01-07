from django.urls import path
from . import views

urlpatterns = [
    path('/upload_digit', views.upload_digit, name = 'upload_digit'),
    path('/test', views.test, name='test')]