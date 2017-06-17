from app import db
from app.models.address import Address


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    phone = db.Column(db.String)
    role = db.Column(db.String)
    gender = db.Column(db.String)
    addresses = db.relationship('Address', backref='person', lazy='dynamic',
                                primaryjoin="User.id == Address.user_id")
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

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
