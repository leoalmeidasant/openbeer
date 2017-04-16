from app import db

class Snack(db.Model):
    __tablename__ = "snacks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    value = db.Column(db.Float)
    type = db.Column(db.String)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime
