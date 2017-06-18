from app import db

class Exchanges(db.Model):
    __tablename__ = "exchanges"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    status = db.Column(db.String)
    delivery_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), index=True)
    fare = db.Column(db.Float)
    total_value = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
