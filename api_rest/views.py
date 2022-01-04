from django.shortcuts import render
from django.http import HttpResponse
from .utils.GetRaports import get_raport
from .utils.GetSecrets import get_secret

URL_portal = get_secret('URL_portal')

def main_page(request):
    data = get_raport(URL_portal, 'espi')
    return HttpResponse(data)


def api_rest(request):
    return HttpResponse("json")