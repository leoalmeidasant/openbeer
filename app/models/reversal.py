from app import db

class Reversal(db.Model):
    __tablename__ = 'reversals'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    value = db.Column(db.Float)
