from crypt import methods
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import to_filename
import services.web_scraping as ws
import json
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bot:bot123@localhost:5432/bot_dev'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    image = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.Text, nullable=False)

    def __init__(self, title, image, location, price, date, url):
        self.title = title
        self.image = image
        self.location = location
        self.price = price
        self.date = date
        self.url = url
    
    def __repr__(self):
        to_string = {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "location": self.location,
            "price": self.price,
            "date": datetime.timestamp(self.date),
            "url": self.url
        }
        return json.dumps(to_string)


@app.route("/search/<string:city>/<string:district>", methods=['GET'])
def search_by_city_district(city, district):
    ads = Announcement.query.first()
    timestamp_db = datetime.timestamp(json.loads(str(ads))['date'])
    ad = ws.search_last_ad(city, district)
    ad = json.loads(ad)
    if(not ads or ad['date'] > timestamp_db):
        dt = datetime.fromtimestamp(ad['date'])
        new_ad = Announcement(ad['title'], ad['image'], ad['location'], ad['price'], dt, ad['url'])
        if(ads):
            db.session.delete(ads)
            db.session.commit()
        else:   
            db.session.add(new_ad)
            db.session.commit()
        return new_ad
        
    return json.loads(str(ads))

@app.route("/search", methods=['GET'])
def search():
    return json.loads(ws.search_last_ad())

@app.route("/districts", methods=['GET'])
def get_districts():
    return json.dumps(ws.get_districts_filter_olx())

