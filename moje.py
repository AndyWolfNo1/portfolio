import requests
from bs4 import BeautifulSoup as bs

url = 'https://infostrefa.com/espi/pl/reports/view/4,499889'

res = requests.get(url)
soup = bs(res.text, 'html.parser')
class_dane = soup.find_all(class_="dane")
cd = class_dane[0].find_all(class_="nTekst")
