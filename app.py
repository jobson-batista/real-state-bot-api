from flask import Flask
from src.controllers.search_controller import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/search")
