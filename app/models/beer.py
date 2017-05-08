from app import db

class Beer(db.Model):
    __tablename__ = "beers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    value = db.Column(db.Float)
    type = db.Column(db.String)
    mark = db.Column(db.String)
    quantity = db.Column(db.Integer)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
