from flask import flash
from flask_login import LoginManager, login_user
from app.core.dao.client_dao import ClientDao

class LoginController(object):
    def __init__(self):
        self.client = ClientDao()

    @staticmethod
    def validate_login(self, username, password):
        user = self.client.validate_login(username, password)
        if not user:
            return {'message': 'Not found'}
        return user
