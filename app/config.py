import os

SECRET_KEY='secretkeytoforms'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
