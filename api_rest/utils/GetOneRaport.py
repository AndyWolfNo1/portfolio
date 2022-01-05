import requests
from bs4 import BeautifulSoup as bs
from .GetSecrets import get_secret

def get_one_raport(nr):
    url_raport = get_secret('URL_raport')
    url_raport = url_raport+nr
    res = requests.get(url_raport)
    soup = bs(res.text, 'html.parser')
    class_dane = soup.find_all(class_="dane")
    cd = class_dane[0].find_all(class_="nTekst")
    data = list()
    for i in cd:
        data.append(i.text.replace('\n', ''))
    return data