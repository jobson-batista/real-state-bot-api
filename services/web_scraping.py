import requests, json, os
from bs4 import BeautifulSoup

OLX_URL_BASE = os.environ.get('OLX_BASE')
headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

def search_last_ad(city='',district=''):
    URL = OLX_URL_BASE
    last_ad = {}
    if(city != '' and district != ''):
        URL = URL+city+'/'+district+'/imoveis'
    else:
        URL = URL+'imoveis'
    try:
        r = requests.get(URL, headers=headers)
        print("\nURL Request: "+r.url+"\n")
    except requests.ConnectionError as e:
        print("Erro ao fazer requisição!\n",e)
    soup = BeautifulSoup(r.content, 'html.parser')
    data_general = soup.find(id='initial-data').get('data-json')
    ad_list = json.loads(data_general)['listingProps']['adList']

    last_ad["title"] = ad_list[0]["subject"]
    last_ad["date"] = ad_list[0]["date"]
    last_ad["location"] = ad_list[0]["location"]
    last_ad["url"] = ad_list[0]["url"]
    last_ad["image"] = ad_list[0]["thumbnail"]
    last_ad["price"] = ad_list[0]["price"].split(" ")[1]

    return json.dumps(last_ad)