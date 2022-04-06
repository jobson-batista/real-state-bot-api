from flask import Flask
import services.web_scraping as ws
import json

app = Flask(__name__)

@app.route("/search/<string:city>/<string:district>", methods=['GET'])
def search_by_city_district(city, district):
    return json.loads(ws.search_last_ad(city, district))

@app.route("/search", methods=['GET'])
def search():
    return json.loads(ws.search_last_ad())