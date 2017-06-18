from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from flask_json import FlaskJSON, JsonError, json_response, as_json

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
ma = Marshmallow(app)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

from app.routes import routes, beers, users, snacks, cart, dashboard, order, exchanges
