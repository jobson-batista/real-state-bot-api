import requests
from bs4 import BeautifulSoup

OLX_URL_BASE = 'https://pb.olx.com.br/paraiba/joao-pessoa/imoveis'

def search():
    headers = {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    r = requests.get(OLX_URL_BASE, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.title)
