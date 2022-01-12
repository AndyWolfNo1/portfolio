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

    def print_raport(r_list):
        dane = dict()
        for i in range(len(r_list)):
            if r_list[i].replace(' ', '') in ['Temat', 'Subject']:
                dane['temat'] = r_list[i + 1]
            if r_list[i].replace(' ', '') in ['Treśćraportu:', 'Contentsofthereport:']:
                dane['tresc'] = r_list[i + 1]
            if r_list[i].replace(' ', '')[:7] == 'Raportb':
                dane['nr'] = r_list[i]
            if r_list[i].replace(' ', '')[:6] in ['Datasp', 'Dateof']:
                dane['data'] = r_list[i]
            if r_list[i].replace(' ', '')[:8] in ['Skrócona', 'Shortnam']:
                dane['nazwa'] = r_list[i + 1]
        return dane

    data = print_raport(data)

    return data