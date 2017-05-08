from app import db
from datetime import datetime
from app.models.beer import Beer
from app.models.snack import Snack

class UpdateStock(object):

    @staticmethod
    def update_beer(id, quantity):
        beer = Beer.query.filter(Beer.id == id).first()
        beer.quantity = beer.quantity - int(quantity)
        beer.updated_at = datetime.today()
        db.session.commit()

    @staticmethod
    def update_snack(id, quantity):
        snack = Snack.query.filter(Snack.id == id).first()
        snack.quantity = snack.quantity - int(quantity)
        snack.updated_at = datetime.today()
        db.session.commit()
