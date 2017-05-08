from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    fare = db.Column(db.Float)
    order_date = db.Column(db.DateTime)
    payment_form = db.Column(db.String)
    total_value = db.Column(db.Float)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
