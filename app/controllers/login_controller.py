from app import app
from flask_login import LoginManager

class LoginController(object):

    def __init__(self):
        self.login_manager = LoginManager()
        self.login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
