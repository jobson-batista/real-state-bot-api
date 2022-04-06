from flask import Flask
from services import web_scraping_service as ws
import json

APP = Flask(__name__)

@APP.route("/search/<string:city>/<string:district>", methods=['GET'])
def search_by_city_district(city, district):
    return json.loads(ws.search_last_ad(city, district))

@APP.route("/search", methods=['GET'])
def search():
    return json.loads(ws.search_last_ad())

if __name__ == '__main__':
    APP.run()