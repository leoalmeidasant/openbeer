from app import db
from app.models.user import User

class UserDao(object):
    def __init__(self):
        pass

    def save(self, user):
        db.session.add(user)
        db.session.flush()

    def update(self, user):
        User.query.filter(User.id == user.id).update(user)
        db.session.commit()
        return 'Success!'

    def delete(self, user_id):
        user = User.query.filter(User.id == user_id).first()
        db.session.delete(user)
        return 'Success!'

    def search(self, user_id=None):
        if not user_id:
            users = User.query.all()
            return users
        else:
            user = User.query.filter(User.id == user_id).first()
            return user

    def validate_login(self, email):
        user = User.query.filter(User.email == email).first()
        return user
