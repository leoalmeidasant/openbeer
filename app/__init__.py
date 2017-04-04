from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')

login_manager = LoginManager()
login_manager.init_app(app)

from app.routes import routes
