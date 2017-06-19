from app import db

class ReturnItens(db.Model):
    __tablename__ = "return_itens"
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String)
    status = db.Column(db.String)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), index=True)
    item = db.relationship('Item')
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), index=True)
    order = db.relationship('Order')
    item_quantity = db.Column(db.Integer)
    item_value = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
