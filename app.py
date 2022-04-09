from flask import Flask, jsonify, request
import services.web_scraping as ws
import json

app = Flask(__name__)

@app.route("/search", methods=['GET'])
def search_by_city_district():
    res = []
    city = request.args.get('city')
    districts_list = request.args.getlist('district')
    for district in districts_list:
        ad = ws.search_last_ad(city, district)
        res.append(json.loads(ad))
    return jsonify(res)        

@app.route("/search", methods=['GET'])
def search():
    return json.loads(ws.search_last_ad())

@app.route("/<string:city>/districts")
def find_all_districts(city):
    return jsonify(ws.get_districts(city))