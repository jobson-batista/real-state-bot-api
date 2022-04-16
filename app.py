from flask import Flask
from src.controllers.search_controller import blueprint
from src.database.database import init_db

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/search")
init_db()
