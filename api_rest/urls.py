from django.contrib import admin
from django.urls import path
from api_rest.views import rest_api
from api_rest.views import main_rest_api

urlpatterns = [
    path('', main_rest_api, name='main_rest_api' ),
    path('<str:s_key>/<str:nr>', rest_api, name='rest_api' ),
]