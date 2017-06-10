from app import db

class ItemOrder(db.Model):
    __tablename__ = "item_orders"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), index=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), index=True)
    item = db.relationship('Item', backref='person')
    returned = db.Column(db.Boolean, default=False)
    confirm_return = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
