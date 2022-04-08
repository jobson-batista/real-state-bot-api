from concurrent.futures import thread
from flask import Flask, jsonify
import services.web_scraping as ws
import json

app = Flask(__name__)
app.run(threaded = True)

@app.route("/search/<string:city>/<string:district>", methods=['GET'])
def search_by_city_district(city, district):
    return json.loads(ws.search_last_ad(city, district))

@app.route("/search", methods=['GET'])
def search():
    return json.loads(ws.search_last_ad())

@app.route("/<string:city>/districts")
def find_all_districts(city):
    return jsonify(ws.get_districts(city))