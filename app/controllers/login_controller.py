from app import app
from flask_login import LoginManager

class LoginController(object):

    def __init__(self):
        pass

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
