from app import db

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, index=True)
    quantity = db.Column(db.Integer)
    value = db.Column(db.Float)
    type = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
