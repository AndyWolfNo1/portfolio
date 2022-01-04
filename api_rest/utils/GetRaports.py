import requests
import numpy
from bs4 import BeautifulSoup as bs

def get_raport(url, name, typ='biezace', date='0,0,0,1'):
    data = list()
    url = url + '/' + name + '/' + typ + ',' + date
    print(url)

    def clean_data(data):
        main_list = list()
        main_list.append(data[0].replace('\n', ''))
        new_list = list()
        for i in range(len(data[1])):
            new_list_b = list()
            td = data[1][i].find_all('td')
            for j in range(len(td)):
                new_list_b.append(td[j].text.replace('\n', ''))
            ahref = data[1][i].find_all('a')
            new_list_b.append(ahref[2]['href'].split(',')[1].split('/')[-1])
            new_list.append(new_list_b)
        main_list.append(new_list)
        return main_list

    def get_tr_from_soup(url):
        resp = requests.get(url)
        soup = bs(resp.text, 'html.parser')
        tabs = soup.find_all('table')
        tr = tabs[1].find_all('tr')
        return tr

    def check_pages(data, url):
        test = numpy.arange(50, 700, 50)
        for i in test:
            if len(data[1]) == i:
                last = int(url[-1]) + 1
                url = url[0:-1]
                url = url + str(last)
                tr = get_tr_from_soup(url)
                for i in tr[2:]:
                    data[1].append(i)
        return data

    tr = get_tr_from_soup(url)
    try:
        today = tr[1].text
        data.append(today)
        data.append(tr[2:])
    except:
        return 'brak banych'
    data = check_pages(data, url)
    data = clean_data(data)
    return data