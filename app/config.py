import os

SECRET_KEY='secretkeytoforms'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
FLASK_APP = os.environ['FLASK_APP']
