from django.shortcuts import render
from django.http import HttpResponse
from .utils.GetRaports import get_raport
from .utils.GetSecrets import generate_s_key
from .utils.GetSecrets import get_secret
from .utils.GetOneRaport import get_one_raport
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

URL_portal = get_secret('URL_portal')

def main_page(request):
    data = get_raport(URL_portal, 'espi')
    day = data[0]
    raports = data[1]

    page = request.GET.get('page', 1)
    paginator = Paginator(raports, 13)
    try:
        raports = paginator.page(page)
    except PageNotAnInteger:
        raports = paginator.page(1)
    except EmptyPage:
        raports = paginator.page(paginator.num_pages)

    return render(request, "main_site.html", {'data' : data, 'day':day, 'raports' : raports})

def main_rest_api(request):
    return render(request, "main_rest_api.html")

def rest_api(request, s_key, nr):
    g_s_key = generate_s_key()
    if s_key == g_s_key.hexdigest():
        if nr:
            try:
                rapo = get_one_raport(str(nr))
  #              return render(request, "test_site.html", {'data': rapo, 'res': g_s_key.hexdigest()})
                return JsonResponse(rapo)
            except:
                return JsonResponse({"massage": "error try get_one-raport"})
        else:
            return JsonResponse({"massage": "error no nr"})

    else:
        return JsonResponse({"massage": "pierwszy if"})
    #    return JsonResponse(content)
    #    return HttpResponse(rapo)
    #    return render(request, "test_site.html", {'data': rapo})
