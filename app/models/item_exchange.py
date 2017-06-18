from app import db

class ItemExchange(db.Model):
    __tablename__ = "item_exchanges"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), index=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchanges.id'), index=True)
    item = db.relationship('Item')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
