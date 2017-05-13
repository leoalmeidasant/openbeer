from app import db

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'),index=True)
    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.id'), index=True)
    quantity = db.Column(db.Integer)
    value = db.Column(db.Float)
    type = db.Column(db.String)
    beer = db.relationship('Beer', backref='person')
    snack = db.relationship('Snack', backref='person')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
