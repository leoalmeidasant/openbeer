from app import db

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String)
    number = db.Column(db.Integer)
    street = db.Column(db.String)
    district = db.Column(db.String)
    city = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
