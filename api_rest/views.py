from django.shortcuts import render
from django.http import HttpResponse
from .utils.GetRaports import get_raport
from .utils.GetSecrets import get_secret
from .utils.GetOneRaport import get_one_raport
from django.http import JsonResponse

URL_portal = get_secret('URL_portal')

def main_page(request):
    data = get_raport(URL_portal, 'espi')
    day = data[0]
    raports = data[1]

    return render(request, "main_site.html", {'data' : data, 'day':day, 'raports' : raports})

def main_rest_api(request):
    return render(request, "main_rest_api.html")

def rest_api(request):
    rapo = get_one_raport('499854')
    content = {'1': rapo}
#    return JsonResponse(content)
#    return HttpResponse(rapo)
    return render(request, "test_site.html", {'data': rapo})