from flask import jsonify, request, Blueprint
from ..services import web_scraping as ws, telegram
import json

blueprint = Blueprint('search_controller', __name__)

@blueprint.route('',methods=['GET'])
def search_by_city_district():
    res = []
    ad = ""
    city = request.args.get('city')
    districts_list = request.args.getlist('district')
    if(districts_list != [] and city != None):
        for district in districts_list:
            ad = ws.search_last_ad(city, district)
    else:
        ad = ws.search_last_ad()
    res.append(json.loads(ad))
    return jsonify(res)        

@blueprint.route("/<string:city>/districts", methods=['GET'])
def find_all_districts(city):
    return jsonify(ws.get_districts(city))

@blueprint.route("/sendAd", methods=['POST'])
def send_ad():
    return telegram.send_ad(request.data)
